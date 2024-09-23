pipeline{
    agent {
                docker { image "python:latest" }
            }
    parameters {
        string(name: 'DOCKER_USERNAME', defaultValue: '', description: 'Login docker')
        password(name: 'DOCKER_PASSWORD', defaultValue: '', description: 'Docker password')
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
                    echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin
                    docker push kabsuri31/pysample
                    docker images
                '''
            }
        }
        stage("Trivy scan"){
            agent {
                docker { image "aquasec/trivy:latest" }
            }
            steps{
                sh '''
                    echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin
                    docker pull kabsuri31/pysample
                    docker images
                    trivy image pysample:1.0 
                '''
            }
        }
    }

}
