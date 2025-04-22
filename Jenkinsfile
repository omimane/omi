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

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests with pytest...'
                bat "\"${PYTHON}\" -m pip install pytest" // Install pytest if not already in requirements.txt
                bat "\"${PYTHON}\" -m pytest tests/ --maxfail=1 --disable-warnings -q"
            }
        }

        stage('Run Streamlit App') {
            steps {
                echo '🚀 Running Streamlit app in background...'
                bat "set STREAMLIT_DISABLE_WELCOME_MESSAGE=true && start \"\" \"${PYTHON}\" -m streamlit run app.py --server.headless true"
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline complete.'
        }
    }
}
