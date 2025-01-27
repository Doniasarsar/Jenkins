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
    }
}
