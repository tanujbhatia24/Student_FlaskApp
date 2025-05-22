pipeline {
    agent any

    environment {
        EC2_HOST = "ec2-user@13.235.79.61"  // 🔁 Replace with your EC2 public IP
        REPO_URL = "https://github.com/tanujbhatia24/Student_FlaskApp.git"
        REMOTE_APP_DIR = "/home/ec2-user/app"
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
                       ssh -o StrictHostKeyChecking=no ec2-user@13.235.79.61 << EOF
                        set -euxo pipefail

                        pkill -f flask || true
                        rm -rf /home/ec2-user/app
                        git clone https://github.com/tanujbhatia24/Student_FlaskApp.git /home/ec2-user/app
                        cd /home/ec2-user/app

                        docker stop flask_app || true
                        docker rm flask_app || true

                        docker build -t student_flaskapp .
                        docker run -d -p 5000:5000 --name flask_app student_flaskapp
                        EOF
                    """
                }
            }
        }
    }

    post {
        success {
            mail to: 'tanujbhatia0001@gmail.com',
                 subject: "✅ SUCCESS: Build #${env.BUILD_NUMBER}",
                 body: "Build succeeded and deployed to EC2. View it at: ${env.BUILD_URL}"
        }
        failure {
            mail to: 'tanujbhatia0001@gmail.com',
                 subject: "❌ FAILURE: Build #${env.BUILD_NUMBER}",
                 body: "Build failed. View it at: ${env.BUILD_URL}"
        }
    }
}
