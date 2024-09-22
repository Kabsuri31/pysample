pipeline{
    
    stages{
        stage("Initialize"){
            agent {
                docker { image "python:latest" }
            }
            steps{
                sh 'python -m venv venv'
                sh 'source /venv/scripts/activate'
                sh 'pip install -r requirements.text'
            }
        }
    }

}
