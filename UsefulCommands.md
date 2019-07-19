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
  add enteries to INSTALLED_APPS

7) Test server (RUN SERVER)
  python manage.py runserver 0.0.0.0:8000

8) Create django model
  - create custom user model AbstractBaseUser, PermissionsMixin
  - specify model manager
9) Create UserProfileManager
10) Configure application to use custom user model
    AUTH_USER_MODEL = 'profiles_api.UserProfile'
    - make migrations
      python manage.py makemigrations profiles_api
    - run migrations
      python manage.py migrate
11) Create super user
12) Add model to admin.py of app



# APIView : CRUD methods
    - full control over the logic
    - calling external APIs

1) Create An API views
2) Configure URL
3) Create serializer


# ViewSet : Common Object Actions
    1) List
    2) Create
    3) Retrieve
    4) Update
    5) Partial Update
    6) Destroy
 
 1) create a viewset
 2) Create routers
 3) Add urls of router to application urls.py
 
#Profile api
1) Create a model serializer
    1) Create meta class : 
        1) Configure serializer to point to a specific model
        2) Add list of fields managed via the serializer 
2) Create a model viewset
    1) provide query set to model viewset
3) Permissions
    1) Create permission
    2) Configure view set to use the permission
    
#Publish to AWS
1) Create ssh
    1) cat ~/.ssh/id_rsa.pub
2) Login to AWS and go to EC2 create Key pair
3) Create Ec2 instance
4) create super user on aws 
    
        sudo env/bin/python manage.py createsuperuser


 
