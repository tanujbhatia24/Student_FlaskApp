pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/tanujbhatia24/Student_FlaskApp.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    docker build -t Student_FlaskApp .
                    docker run -d -p 5000:5000 --name flask_app Student_FlaskApp
                '''
            }
        }
    }


    post {
        success {
            mail to: 'tanujbhatia0001@gmail.com',
                 subject: "✅ SUCCESS: Build #${env.BUILD_NUMBER}",
                 body: "Build succeeded. View it at: ${env.BUILD_URL}"
        }
        failure {
            mail to: 'tanujbhatia0001@gmail.com',
                 subject: "❌ FAILURE: Build #${env.BUILD_NUMBER}",
                 body: "Build failed. View it at: ${env.BUILD_URL}"
        }
    }
}