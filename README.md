# robot-project


## Linux Setup Instructions

Install some required packages:

'''
sudo apt update & sudo apt upgrade -y
sudo apt install git python3 python3-pip
'''

Clone the project and move into the project directory:

'''
git clone https://github.com/plb538/robot-project.git
cd robot-project/
'''

Create your virtual environment:

'''
mkdir venv
python3 -m venv venv/
'''

Source your virtual environment and install the required modules:

'''
source venv/bin/activate
pip3 install -r requirements.txt
'''

### Useful Git Links

[Do not run the 'git init' command]

(http://rogerdudler.github.io/git-guide/)
(https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

