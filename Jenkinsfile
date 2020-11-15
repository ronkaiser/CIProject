pipeline {
  agent any
  stages {
    stage('preperation') {
      steps {
        //git clone will be done automatically 
        echo 'verify the user input file'
        script {
           def inputCSVPath = input message: 'Upload file', parameters: [file(name: 'Test.csv', description: 'Upload only CSV file')]
           def csvContent = readFile "${inputCSVPath}"
           echo ("CSV FILE PATH IS : ${inputCSVPath}")
           echo("CSV CONTENT IS: ${csvContent}") 
        }
      }
    }
    stage('ansible') {
      steps {
        sh 'ansible-playbook -i ./ansible/inventory ./ansible/setup.yml'
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
