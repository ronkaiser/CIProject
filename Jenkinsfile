pipeline {
  agent any
  stages {
    stage('preperation') {
      steps {
        //git clone will be done automatically 
        cleanWS()
        echo 'verify the user input file'
      }
    }
    stage('ansible') {
      steps {
        sh 'ansible-playbook -i ./ansible/inventory ./ansible/setup.yml'
      }
    }
    stage('whats_going_on') {
      steps {
        sh 'python3 ./whats_going_on.py > ~/results.json'
      }
    }
  }
}
