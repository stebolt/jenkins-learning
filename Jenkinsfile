pipeline {
  agent any
  
  environment {
      RELEASE='22.10'
  }
  
  stages {
    stage('Build') {
      environment {
          LOG_LEVEL='INFO'
      }
      parallel {
        stage('linux-arm64') {
          steps {
            echo "Building release ${RELEASE} for ${STAGE_NAME} with log level ${LOG_LEVEL}..."
          }
        }
        stage('linux-amd64') {
          steps {
            echo "Building release ${RELEASE} for ${STAGE_NAME} with log level ${LOG_LEVEL}..."
          }
        }
        stage('windows-amd64') {
          steps {
            echo "Building release ${RELEASE} for ${STAGE_NAME} with log level ${LOG_LEVEL}..."
          }
        }
      }
    }
    stage('Test') {
      steps {
        echo "Testing release ${RELEASE}..."
        writefile file: 'test-results.txt', text: 'passed'
      }
    }
    stage('Deploy') {
      input {
        message 'Deploy?'
        ok 'Do it!'
        parameters {
            string(name: 'TARGET_ENVIRONMENT', defaultValue: 'PROD', description: 'Target deployment environment')
        }
      }
      steps {
        echo "Deploying release ${RELEASE} to environment ${TARGET_ENVIRONMENT}"
      }
    }
  }
  post{
    always {
      echo 'Prints whether deploy happens or not, success or failure'
    }
  }
}
