pipeline {
    agent any

    environment {
        EC2_HOST = "ec2-user@43.204.236.54"  // Replace with your EC2 public IP
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
                        echo "Connected to EC2 as: \$(whoami)"
                        mkdir -p ${REMOTE_APP_DIR}
                        cd ${REMOTE_APP_DIR}

                        if [ -d "${REPO_APP_DIR}/.git" ]; then
                            echo "Repo exists. Pulling latest changes!"
                            cd ${REPO_APP_DIR}
                            git reset --hard HEAD
                            git pull origin main
                        else
                            echo "Cloning fresh repo!"
                            git clone ${REPO_URL}
                        fi

                        cd ${REPO_APP_DIR}

                        echo "Updating .env file!"
                        cat > .env <<EOL
        MONGO_URI=${MONGO_URI}
        PORT=5000
        EOL

                        echo ".env updated:"
                        cat .env 
                    '
                """
                }
            }
        }
    }
}
