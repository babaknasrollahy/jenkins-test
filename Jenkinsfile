pipeline{
  agent any
  stages{
    stage('Clone Source Code'){
      steps{
        git brache: 'main', url:'https://github.com/babaknasrollahy/jenkins-test.git'
      }
      stage('Dockerize'){
      steps{
        sh 'docker build -t test:latest .'
      }
    }
  }
}
