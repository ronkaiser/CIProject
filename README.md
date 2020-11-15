# CIProject
CI project
Prestep:
- assuming that ansible will ssh localhost using jenkins user by generating ssh key

Jenkins setup:
--------------

- Virtual Box and Vagrant installation

- initialize Vagrant environment using ubuntu/bionic64 based on ubuntu 18.04LTS

- Edit Vagrant file - adding private network adapter and port forward configuration 8080 (Jenkins default)

- Jenkins + Java installation

- Suggested plugins installed

- since that image came with python3 I've installed only Ansible

Git repository:
---------------

- I've open new repository in my GitHub account 

- Initialized local folder with all required files, add, commit and push to my GitHub repository

Jenkins server:
---------------
- On Jenkins server I've cloned my repository to test each file separately before automation configuration in Jenkins
