pipeline{
    agent {
                docker { image "python:latest" }
            }
    stages{
        stage("Initialize"){
            
            steps{
                sh 'python -m venv venv'
                sh 'ls'
                sh './venv/bin/pip3 install --upgrade --requirement requirements.txt'
            }
        }
        stage("Test"){
            steps{
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=results.xml
                '''
            }
        }
        stage("Build Image"){
            steps{
                sh '''
                    docker build -t pysample:1.0 .
                    docker images
                '''
            }
        }
    }

}
