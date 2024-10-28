pipeline {
    agent any

    environment {
        VENV = 'venv'  // Virtual environment directory
        DATA_PATH = 'path/to/dataset/entree+chicago+recommendation+data'  // Path to your data
    }

    stages {
        stage('Setup') {
            steps {
                // Step to clone the repository
                git url: 'https://your-repo-url.git'

                // Install dependencies in a virtual environment
                sh '''
                    python3 -m venv $VENV
                    source $VENV/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Data Preprocessing') {
            steps {
                // Run data preprocessing script
                sh '''
                    source $VENV/bin/activate
                    python3 data_preprocessing.py --data $DATA_PATH
                '''
            }
        }

        stage('Model Training') {
            steps {
                // Run model training script
                sh '''
                    source $VENV/bin/activate
                    python3 model_training.py
                '''
            }
        }

        stage('Model Evaluation') {
            steps {
                // Run evaluation script
                sh '''
                    source $VENV/bin/activate
                    python3 evaluation.py
                '''
            }
        }

        stage('Deployment') {
            steps {
                // Run deployment script
                sh '''
                    source $VENV/bin/activate
                    python3 deploy.py
                '''
            }
        }
    }

    post {
        always {
            // Clean up virtual environment
            sh 'rm -rf $VENV'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the logs for more details.'
        }
    }
}
