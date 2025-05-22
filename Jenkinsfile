pipeline {
    agent any

    environment {
        EC2_HOST = "ec2-user@13.235.79.61"  // 🔁 Replace with your EC2 public IP
        REPO_URL = "https://github.com/tanujbhatia24/Student_FlaskApp.git"
        REMOTE_APP_DIR = "/home/ec2-user/app"
        REPO_APP_DIR = "/home/ec2-user/app/Student_FlaskApp"
        DOCKER_IMAGE = "student_flaskapp"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'venv/bin/pytest test_app.py --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent (credentials: ['tanuj-ec2-ssh-key']) {  // 🔁 Replace with your SSH credential ID in Jenkins
                    sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_HOST} " 
                            set -euxo pipefail
                            echo ✅ Connected to EC2!
                            pkill -f flask || true
                            rm -rf ${REMOTE_APP_DIR}
                            git clone ${REPO_URL} ${REMOTE_APP_DIR}
                            cd ${REMOTE_APP_DIR}
                            docker stop flask_app || true
                            docker rm flask_app || true
                            docker build -t ${DOCKER_IMAGE} .
                            docker run -d -p 5000:5000 --name flask_app ${DOCKER_IMAGE}
                        "
                    """
                }
            }
        }
    }
}
