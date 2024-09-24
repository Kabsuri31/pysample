pipeline{
    agent {
                docker { image "python:latest" }
            }
    environment {
        SONAR_HOST_URL = 'http://172.17.0.3:9000'  
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
        /*stage("Test"){
            steps{
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=results.xml
                '''
            }
        }*/
        stage("Build Image"){
            steps{
                sh '''
                    docker build -t kabsuri31/pysample:1.0 .
                    echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin
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
        stage("Run application"){
            steps{
                script{
                    def containerName = 'pysample'
                    def isRunning = sh (
                        script: "docker ps --filter 'name=${containerName}' --format '{{.Names}}'",
                        returnStdout: true
                    ).trim()
                    if (isRunning != containerName) {
                    sh('''
                        docker run -d --name pysample -p 8090:5000  kabsuri31/pysample:1.0
                        docker ps -a
                        '''
                        )
                    }
                    
                        def containerIp = sh (
                                script: "docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pysample",
                                returnStdout: true
                            ).trim()
                        env.CONTAINER_IP = containerIp
                        sh("echo ${env.CONTAINER_IP}")
                    }
            }
        }
       /* stage("Sonar scan"){
            agent {
                docker { image 'sonarsource/sonar-scanner-cli' }
            }
            steps{
                script {
                    withSonarQubeEnv('SonarQubeScanner') {  
                        sh """
                        sonar-scanner \
                          -Dsonar.host.url=${SONAR_HOST_URL} \
                          -Dsonar.login=${SONAR_LOGIN}
                        """
                    }
            }
        }
    }*/
    stage("Load Testing -> Jmeter"){
        steps{
            dir("${env.WORKSPACE}"){
                sh '''
                    ls -l ./tests
                    docker run --rm -v ./tests:/tests justb4/jmeter:5.5 -n -t /tests/flask_test_plan.jmx -l /tests/result.jtl
                '''
            }
        }
    }
 
   }

}
 
