pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/mohanDevOps-arch/Student_App.git'
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
                sh 'nohup python app.py &'
            }
        }
    }
}
