pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\OMKAR\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
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
                echo '📦 Installing dependencies from requirements.txt...'
                bat "\"${PYTHON}\" -m pip install --upgrade pip"
                bat "\"${PYTHON}\" -m pip install -r requirements.txt"
            }
        }

        stage('Run Streamlit App') {
            steps {
                echo '🚀 Running Streamlit app in headless mode...'
                bat "set STREAMLIT_DISABLE_WELCOME_MESSAGE=true && \"${PYTHON}\" -m streamlit run app.py --server.headless true"
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline complete.'
        }
    }
}

