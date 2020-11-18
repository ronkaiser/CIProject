# CIProject
CI project

Jenkins setup:
--------------
- Virtual Box and Vagrant installation
- initialize Vagrant environment using ubuntu/bionic64 based on ubuntu 18.04LTS
- Edit Vagrant file - adding private network adapter and port forward configuration 8080 (Jenkins default port)
- Jenkins + Java installation
- Suggested plugins installed
- since that image came with python3 I've installed only Ansible
- create Pipeline job and add SCM git repo 
- change Branches to build from master to main
- assuming that Ansible will ssh to localhost using Jenkins user by generating ssh key

Jenkins plugins:
----------------
- No need additional plugins

Git repository:
---------------
- Creating new repository in my GitHub account 
- Initialized local folder with all required files, add, commit and push to my GitHub repository

Jenkins server:
---------------
- On Jenkins server I've cloned my repository manually to test each file separately before automation configuration in Jenkins

Pipeline description:
---------------------
- My pipeline built with 5 stages: Preparation, Ansible, whats_going_on and post function that delete the cloned git repository

Preperation:
In this stage Jenkins asking the user to upload valid key, next reading the file content and add it to variable, then printing the path and the content (that was also useful for my test) and after that it create additional file with the same content so it can read from in the next stage.
The final step is validating the upload key and print informative error in case the input file isn't key.

Ansible:
In this stage jenkins executing Ansible playbook using inventory file (in this case localhost) and setup.yml file 
That playbook written with loop in case we want to add more users in the future.
Currently it create user named bob with password, next task is generating key by authorization key module (was created for my tests), then creates file include content with read only permissions to bob user.
And the final step was to search the file that uploaded in stage one and add the content to bob's authorized keys.

whats_going_on:
In this stage jenkins executing python script called whats_going_on.py and send the output to workspace directory by creating file named results.jason 
In the script I'm using various python libraries, each of them provided the required info parameters and json lib used to phrase the output into json file format by indentation function and dump all the info that shown in dictionary by keys and values.
