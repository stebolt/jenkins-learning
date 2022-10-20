pipeline {
  agent any
  stages {
    stage('Stage1') {
      steps {
        sh 'echo "this is $BUILD_NUMBER of demo $DEMO"'
      }
    }

  }
  environment {
    DEMO = '1'
  }
}