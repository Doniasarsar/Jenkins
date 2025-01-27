pipeline {
    agent any
    environment {
        CONTAINER_ID = '' // Variable pour stocker l'ID du conteneur
        SUM_PY_PATH = './sum.py' // Remplacez par le chemin de sum.py
        DIR_PATH = '' // Chemin vers le répertoire contenant le Dockerfile
        TEST_FILE_PATH = '' // Chemin vers le fichier de test
    }
    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh """
                    docker build -t python-sum-app ${DIR_PATH}
                """
            }
        }
        //stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                script {
                    CONTAINER_ID = sh(script: "docker run -dit python-sum-app", returnStdout: true).trim()
                }
                echo "Container ID: ${CONTAINER_ID}"
            }
        //}
        //stage('Test sum.py') {
            steps {
                echo 'Testing sum.py with input values...'
                script {
                    // Lire le fichier de test et exécuter les tests
                    def testFile = readFile("${TEST_FILE_PATH}")
                    testFile.eachLine { line ->
                        def args = line.split(' ')
                        def output = sh(script: "docker exec ${CONTAINER_ID} python /app/sum.py ${args[0]} ${args[1]}", returnStdout: true).trim()
                        echo "Input: ${args[0]}, ${args[1]} -> Output: ${output}"
                    }
                }
            }
        //}
        //stage('Cleanup') {
            steps {
                echo 'Cleaning up...'
                sh """
                    docker stop ${CONTAINER_ID}
                    docker rm ${CONTAINER_ID}
                """
            }
        //}
    }
}
