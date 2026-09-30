pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .jenkins-venv
                    . .jenkins-venv/bin/activate

                    pip install --upgrade pip
                    pip install -r app/requirements.txt
                    pip install pytest

                    PYTHONPATH=. pytest -q
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build \
                        -t devops-demo:${BUILD_NUMBER} \
                        -t devops-demo:latest .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker compose up -d --build
                '''
            }
        }

        stage('Health Check') {
    steps {
        sh '''
            echo "Waiting for application..."
            sleep 10

            echo "Checking Docker Compose services..."
            docker compose ps

            echo "Checking Nginx health..."
            docker compose exec -T nginx wget -qO- http://localhost/health
        '''
    }
}

    post {

        success {
            echo '================================='
            echo 'DEPLOYMENT SUCCESSFUL!'
            echo '================================='
        }

        failure {
            echo '================================='
            echo 'PIPELINE FAILED!'
            echo '================================='
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
