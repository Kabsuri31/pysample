pipeline{
    agent {
                docker { image "python:latest" }
            }
    environment {
        SONAR_PROJECT_KEY = 'pysample'  
        SONAR_HOST_URL = 'http://localhost:9000'  
        SONAR_LOGIN = credentials('sonarqube-token-id') 
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
                    docker build -t kabsuri31/pysample:1.0 .
                    echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin
                    docker push kabsuri31/pysample:1.0
                    docker images
                '''
            }
        }
        /*
        stage("Trivy scan"){
            steps{
                sh '''
                    echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin
                    docker pull kabsuri31/pysample:1.0 
                    docker images
                    docker run aquasec/trivy --severity HIGH,CRITICAL image kabsuri31/pysample:1.0
                '''
            }
        }*/
        stage("Sonar scan"){
            steps{
                script {
                    withSonarQubeEnv('SonarQubeScanner') {  
                        sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner " +
                           "-Dsonar.projectKey=${SONAR_PROJECT_KEY} " +
                           "-Dsonar.sources=. " +
                           "-Dsonar.host.url=${SONAR_HOST_URL} " +
                           "-Dsonar.login=${SONAR_LOGIN}"
                    }
            }
        }
    }
    }

}
