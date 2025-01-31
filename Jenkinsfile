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
                    echo "Building Docker image..."
                    sh """
                        docker build -t sum-calculator ${DIR_PATH}
                    """
                }
            }
        }
    
        stage('Run') {
            steps {
                script {
                    echo "Running Docker container..."
                    def output = sh(script: "docker run -d -it sum-calculator sh", returnStdout: true).trim()
                    env.CONTAINER_ID = output
                    echo "Container ID: ${env.CONTAINER_ID}"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Starting tests..."
                    def testLines = readFile(env.TEST_FILE_PATH).split('\n')
                    for (line in testLines) {
                        def vars = line.split(' ')
                        def arg1 = vars[0]
                        def arg2 = vars[1]
                        def expectedSum = vars[2].toFloat()

                        def output = bat(
                            script: "docker exec ${env.CONTAINER_ID} python /app/sum.py ${arg1} ${arg2}",
                            returnStdout: true
                        ).trim()

                        def result = output.toFloat()
                        if (result == expectedSum) {
                            echo "Test passed: ${arg1} + ${arg2} = ${result}"
                        } else {
                            error "Test failed: ${arg1} + ${arg2} != ${result}"
                        }
                    }
                }
            }
        }



        
    }
}
