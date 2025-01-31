pipeline {
    agent any

    environment {
        PATH = "/Users/doniasarsar/.docker/bin:$PATH" // Ajoutez ce chemin
        CONTAINER_ID = ""
        SUM_PY_PATH = "./sum.py"
        DIR_PATH = "./"
        TEST_FILE_PATH = "./test_variables.txt"
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
                    
                    // Démarrer le conteneur et capturer l'ID de manière fiable
                    def containerOutput = sh(script: "docker run -d -it sum-calculator sh", returnStdout: true).trim()
                    
                    if (!containerOutput || containerOutput.isEmpty()) {
                        error "❌ Échec du démarrage du conteneur Docker : aucun ID récupéré."
                    }

                    env.CONTAINER_ID = containerOutput
                    echo "✅ Container ID: ${env.CONTAINER_ID}"

                    // Vérifier que le conteneur tourne bien
                    def checkContainer = sh(script: "docker ps --filter id=${env.CONTAINER_ID} --format '{{.ID}}'", returnStdout: true).trim()
                    
                    if (!checkContainer || checkContainer.isEmpty()) {
                        error "❌ Le conteneur ${env.CONTAINER_ID} ne tourne pas correctement."
                    }

                    echo "🎯 Conteneur démarré avec succès !"
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
