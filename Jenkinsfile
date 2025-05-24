pipeline {
    agent any

    environment {
        EC2_HOST = "ec2-user@13.235.79.61"  // Replace with your EC2 public IP
        REPO_URL = "https://github.com/tanujbhatia24/Student_FlaskApp.git"
        REMOTE_APP_DIR = "/home/ec2-user/app"
        REPO_APP_DIR = "/home/ec2-user/app/Student_FlaskApp"
        DOCKER_IMAGE = "student_flaskapp"
        MONGO_URI = credentials('tanuj-MONGO-URI')  // 👈 Use Jenkins credentials
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running tests with MONGO_URI=${MONGO_URI}"
                    MONGO_URI=${MONGO_URI} venv/bin/pytest test_app.py --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent (credentials: ['tanuj-ec2-ssh-key']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_HOST} '
                            set -xe
                            echo "Connected to EC2!"
                            rm -rf ${REMOTE_APP_DIR}
                            git clone ${REPO_URL} ${REMOTE_APP_DIR}
                            cd ${REPO_APP_DIR}
                            echo "Creating .env file!"
                            cat > .env <<EOL
MONGO_URI=${MONGO_URI}
PORT=5000
EOL
                            echo ".env file created!"
                            ls -la
                            cat .env
                        '
                    """
                }
            }
        }
    }
}
