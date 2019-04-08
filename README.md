# robot-project


## Linux Setup Instructions

Install some required packages:
```
sudo apt update & sudo apt upgrade -y
sudo apt install git python3 python3-pip python3-venv
```

Tell Git who you are:
```
git config --global user.name "<your name>"
git config --global user.email "<your email>"
```

Clone the project and move into the project directory:
```
git clone https://github.com/plb538/robot-project.git
cd robot-project/
```

Create your virtual environment:
```
mkdir venv
python3 -m venv venv/
```

Source your virtual environment and install the required modules:
```
source venv/bin/activate
pip3 install -r requirements.txt
```

Test it out!
```
./robot_project/main.py
```

### Useful Git Links

**Do not run the 'git init' command**

* http://www.rogerdudler.github.io/git-guide
* https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet

### Useful Linux Commands

**NOTE**: Use the '--help' option with any command to see additional arguments.

```
ls (List the contents of a directory)
cd (Move to another directory)
pwd (Show where you are in the file system)
cp (Copy a file)
mv (Move a file)
rm (Remove a file)

mkdir (Make a directory)
rmdir (Remove a directory)

history (Show your command history)

touch (Make a file)
grep (Seach a file)
find (Find a file)

top (Display process and cpu usage)
free (Display memory usage)
df (Display disk usage)

chmod (Change file permissions)
chown (Change file ownership)
```

Some useful networking commands:
```
ifconfig
ip addr
ip route
route
```

Some useful package management commands:
```
sudo apt update
sudo apt upgrade
sudo apt search
sudo apt install
```
