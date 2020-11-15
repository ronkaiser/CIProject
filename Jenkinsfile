pipeline {
  agent any
  stages {
    stage('preperation') {
      steps {
        //git clone will be done automatically 
        echo 'verify the user input file'
      }
    }
    stage('ansible') {
      steps {
        sh 'ansible-playbook ./ansible/setup.yml'
      }
    }
    stage('whats_going_on') {
      steps {
        sh 'python3 ./whats_going_on.py > results.json'
      }
    }
  }
  post {
    always {
            echo 'One way or another, I have finished'
            deleteDir() /* clean up our workspace */
        }
    }
}
