# robot-project


## Linux Setup Instructions

Install some required packages:
```
sudo apt update & sudo apt upgrade -y
sudo apt install git python3 python3-pip python3-venv python3-dev
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

## Development Workflow

### Basics

Make sure you are in the project directory (i.e. .../robot-project/) and you have your python environment sourced (```source venv/bin/activate```).

Use the ```git status``` command to see created/deleted/modified files.

Use the ```git branch``` command to see what branch you are using.

Use the ```git checkout <branch name>``` command to change which brach you are using.

### How To Add To The Project

To start, ensure your local copy of the master branch is up-to-date with Github's version:
```
git branch
```

If you are **not** on the master branch:
```
git checkout master
``` 

Once on the **master** branch, **pull** the latest changes from Github:
```
git pull
```

Make sure your python environment has all of its requirements:
```
pip install -r requirements.txt
```

Now that you have the latest changes, its time to create a new branch to work on:
```
git checkout -b <new branch name>  # The '-b' argument creates a new branch, and the checkout command switches to that new branch
```

Now make your changes on your new branch. When you are ready to add to the project, you must create a **Pull Request (PR)**.

Save your changes and create your commit. Make sure you are on **your branch** and **not master**:
```
git status  # See modifications made to your branch
git add --all  # Add the modifications you wish to commit (in this case all)
git commit -sm "<A detailed message of the change you are proposing>"
```

You can make **multiple commits** before you are ready to **push**. When you are ready, run the following command:
```
git push origin --set-upstream <branch name> 
```

From here, we will see it on Github.

## Useful Git Links

**Do not run the 'git init' command**

* http://www.rogerdudler.github.io/git-guide
* https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet

## Useful Linux Commands

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
