pipeline {
  agent any
  stages {
    stage('preperation') {
      steps {
        //git clone will be done automatically 
        echo 'verify the user input file'
          script {
          // def inFile = input id: 'file1', message: 'Upload a file', parameters: [file(name: 'data.tmp', description: 'Choose a file')]
          def inFile = input message: 'Upload file', parameters: [file(name: 'data.tmp', description: 'Upload public key file')]
          data = readFile(file: "${inFile}")
          echo ("KEY FILE PATH IS : ${inFile}")
          echo("KEY CONTENT IS: ${data}") 
          // Check if file valid public key
          def stdout = sh returnStdout: true, script: "ssh-keygen -l -f ${inFile}"
          echo("${stdout}")
        }
      }
    }
    stage('ansible') {
      steps {
        //sh 'ansible-playbook -i ./ansible/inventory ./ansible/setup.yml --extra-vars "ssh_public_key=${data}"'
        echo '${data}'
        sh 'ansible-playbook -i ./ansible/inventory ./ansible/setup.yml --extra-vars "ssh_public_key=${data}"'
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
