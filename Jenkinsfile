pipeline {
    agent any

    environment {
        CONTAINER_ID = '' // Variable pour stocker l'ID du conteneur
        SUM_PY_PATH = './sum.py' // Chemin vers le script sum.py
        DIR_PATH = './' // Chemin vers le répertoire contenant le Dockerfile (par défaut, le répertoire courant)
        TEST_FILE_PATH = './test_variables.txt' // Chemin vers le fichier de test
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    if (DIR_PATH == '') {
                        error "DIR_PATH is not set. Please define the path to your Dockerfile."
                    }
                }
                echo 'Building Docker image...'
                sh """
                    docker build -t python-sum-app ${DIR_PATH}
                """
            }
        }
    }
}
