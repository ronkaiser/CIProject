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
        sh 'sudo ansible-playbook -i ./inventory ./ansible/setup.yml'
      }
    }
    stage('whats_going_on') {
      steps {
        sh 'python3 ./whats_going_on.py > /var/lib/jenkins/workspace/results.json'
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
