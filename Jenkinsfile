pipeline{
    agent any
    stages{
        stage("Initialize"){
            agent {
                docker { image "python:latest" }
            }
            steps{
                sh 'python -m venv venv'
                sh 'pwd'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.text'
            }
        }
    }

}
