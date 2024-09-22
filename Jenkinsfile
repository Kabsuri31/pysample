pipeline{
    agent any
    stages{
        stage("Initialize"){
            agent {
                docker { image "python:latest" }
            }
            steps{
                sh 'python -m venv venv'
                sh 'ls'
                sh 'source ./venv/bin/activate'
                sh 'pip install -r requirements.text'
            }
        }
    }

}
