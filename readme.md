# new system libraries
sudo apt install python3-venv
$sudo apt install gitk 

# new system setup ssh-key
- Generate ssh key
ssh-keygen -t ed25519 -C "somanathg238@gmail.com"
- copy the .pub ssh key content 
cat /home/somanath/.ssh/id_ed25519.pub
- Add ssh key in github https://github.com/settings/keys

# new user confignation

- git config --global user.name "Somanath" 
- git config --global user.email "somanathg238@gmail.com"


# For each project
git init (new repo initialisation)
git remote add origin git@github.com:somanathgumudi/resume-app-flask.git
git branch -M main

python3 -m venv venv
source venv/bin/activate
pip install Flask
or
pip install -r requirements.txt

# With each code change
source venv/bin/activate


git status  or gitk
git add app.py or git add --all
git status
git commit -m "flask app"
git push origin main
git pull origin main


# other commands
history

# run the app
source venv/bin/activate
python app.py

http://127.0.0.1:5000/hello
http://localhost:5000/hello
http://0.0.0.0:5000/hello


ifconfig

copy inet address eg 192.168.114.147


http://192.168.114.147:5000/hello