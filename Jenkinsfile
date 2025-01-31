pipeline {
    agent any

    environment {
        PATH = "/Users/doniasarsar/.docker/bin:$PATH" // Ajoutez ce chemin si nécessaire
        CONTAINER_ID = ""
        SUM_PY_PATH = "./sum.py"
        DIR_PATH = "./"
        TEST_FILE_PATH = "./test_variables.txt"
        DOCKERHUB_REPO = "votre_nom_dockerhub/sum-calculator" // Remplacez par votre identifiant DockerHub
    }

    stages {
        stage('Build') {
            steps {
                script {
                    echo "🚀 Building Docker image..."
                    sh """
                        docker build -t sum-calculator ${DIR_PATH}
                    """
                }
            }
        }
    
        stage('Run') {
            steps {
                script {
                    echo "🔄 Running Docker container..."
                    
                    // Démarrer le conteneur et récupérer l'ID
                    def output = sh(script: "docker run -d -it sum-calculator sh", returnStdout: true).trim()
                    env.CONTAINER_ID = output
                    echo "✅ Container ID: ${env.CONTAINER_ID}"

                    // Vérifier que le conteneur est bien en cours d'exécution
                    sh "docker ps -a --filter id=${env.CONTAINER_ID}"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "🧪 Starting tests..."
                    def testLines = readFile(env.TEST_FILE_PATH).split('\n')

                    for (line in testLines) {
                        if (line.trim()) { // Vérifier que la ligne n'est pas vide
                            def vars = line.split(' ')
                            def arg1 = vars[0]
                            def arg2 = vars[1]
                            def expectedSum = vars[2].toFloat()

                            echo "🔢 Testing: ${arg1} + ${arg2} = ${expectedSum}"

                            // Exécuter sum.py dans le conteneur Docker
                            def output = sh(script: "docker exec ${env.CONTAINER_ID} python /app/sum.py ${arg1} ${arg2}", returnStdout: true).trim()
                            def result = output.toFloat()

                            if (result == expectedSum) {
                                echo "✅ Test réussi : ${arg1} + ${arg2} = ${result}"
                            } else {
                                error "❌ Test échoué : ${arg1} + ${arg2} = ${result} (attendu: ${expectedSum})"
                            }
                        }
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "📦 Déploiement de l'image sur DockerHub..."

                    // Connexion à DockerHub (Stockez les identifiants dans Jenkins)
                    sh "docker login -u \$DOCKERHUB_USERNAME -p \$DOCKERHUB_PASSWORD"

                    // Taguer l’image avant de la pousser
                    sh "docker tag sum-calculator ${DOCKERHUB_REPO}:latest"

                    // Pousser l’image sur DockerHub
                    sh "docker push ${DOCKERHUB_REPO}:latest"

                    echo "✅ Image poussée avec succès sur DockerHub : ${DOCKERHUB_REPO}:latest"
                }
            }
        }
    }

    post {
        always {
            script {
                echo "🧹 Nettoyage : Suppression du conteneur..."
                sh "docker stop ${env.CONTAINER_ID} || true"
                sh "docker rm ${env.CONTAINER_ID} || true"
            }
        }
    }
}
