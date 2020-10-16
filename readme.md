1]install python>=3.6
windows : download from official python website, add to PATH env variable
linux : sudo apt-get install python3.6

2]install virtualev
windows cmd : py -3.6 -m pip install virtualenv
linux : sudo pip3 install virtualenv or sudo python36 -m pip install virtualenv

3]create virtual environment
go to the folder where you want to create this project >
right click > 
windows power shell > 
windows cmd : py -3.6 -m virtualenv env_cmax
linux : virtualenv -p /usr/bin/python3.6 env_cmax
//your virtual env name is env_cmax here

4]open vscode (in same folder as step 3])
go to the folder where you want to create this project >
right click > 
windows power shell > 
windows cmd>code .
linux : code .

py -3.6 manage.py runserver


