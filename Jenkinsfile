pipeline{
  agent any
  stages{
    
    stage('Clone Source Code'){
      steps{
        git branch: 'main', url:'https://github.com/babaknasrollahy/jenkins-test.git'
      }
    }
    
      stage('Dockerize'){
        steps{
          sh 'docker-compose up'
        }
      }
    
      stage('removing'){
          steps{
            sh 'docker-compose rm -f'
            sh 'docker image rm bazipipeline_test'
          }
      }
  }
}

