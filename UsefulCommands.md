# Useful Commands for this project

1) Create a git ignore file
2) Create local server using vagrant
  - create a vagrant file with required ubuntu
      vagrant init ubuntu/bionic64
  - configure vagrant file
  - start server
      vagrant up
  - connect to server
      vagrant ssh
  - disconnect
      exit
  - access project folder on virtual machine vagrant folder is synched with project folder
    cd /vagrant

3) Create a python virtual enviornment
  - go to vagrant folder on VM and type
      python -m venv ~/env
  - activate env
      source ~/env/bin/activate

4) Install requirement for projects
  - create requirements.txt
    pip install -r requirements.txt

5) Start a project
  - create project
    django-admin startproject profiles_project .
  - create an app
    python manage.py startapp profiles_api

6) Enable app on project settings
