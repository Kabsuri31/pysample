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
                sh './venv/bin/pip3 install --upgrade --requirement requirements.txt'
            }
        }
        stage("Test"){
            steps{
                dir("${env.WORKSPACE}"){
                    sh 'ls -l /venv/bin'
                    sh './venv/bin/pytest'
                }                
            }
        }
    }

}
