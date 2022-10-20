pipeline {
  agent any
  
  environment {
      DEMO='1.3'
  }
  
  stages {
    stage('Stage-1') {
      steps {
        sh 'echo "this is $BUILD_NUMBER of demo $DEMO"'
        sh '''
            echo "Using a multi-line shell step"
        '''
      }
    }
  }
}
