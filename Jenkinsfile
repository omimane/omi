pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning Repository...'
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                echo 'Setting up Python Virtual Environment...'
                sh 'python -m venv $VENV_DIR'
                sh '. $VENV_DIR/bin/activate && pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '. $VENV_DIR/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Streamlit App') {
            steps {
                echo 'Running Streamlit App...'
                sh '. $VENV_DIR/bin/activate && streamlit run app.py'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf $VENV_DIR'
        }
    }
}
