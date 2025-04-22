pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\OMKAR\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
        REPO_URL = 'https://github.com/omimane/omi.git'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo '📥 Cloning GitHub repository...'
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                bat "${PYTHON_PATH} -m pip install --upgrade pip"
                bat "${PYTHON_PATH} -m pip install -r requirements.txt"
            }
        }

        stage('Run Streamlit App') {
            steps {
                echo '🚀 Running the Streamlit app...'
                bat "streamlit run app.py"
            }
        }

        // Optional test/deploy stages can go here
    }

    post {
        always {
            echo '✅ Pipeline complete.'
        }
    }
}
