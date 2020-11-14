pipeline {
  agent any
  stages {
    stage('preperation') {
      steps {
        sh 'git clone https://github.com/ronkaiser/CIProject.git'
      }
    }
    stage('ansible') {
      steps {
        sh 'ansible-playbook -i ./CIProject/inventory ./CIProject/setup.yml'
      }
    }
    stage('whats_going_on') {
      steps {
        sh 'python3 ./CIProject/whats_going_on.py > results.json'
      }
    }
  }
}
