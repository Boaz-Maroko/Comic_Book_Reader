# Step One (Installing python)
## Windows
Install the latest version of python (`required version 3.12`) from the windows store or 
from the [official python website](https://www.python.org/downloads/).

If downloaded from the official store make sure to check add **PYTHON TO PATH** during install
setup.

## Linux
Go to the Terminal and run 
```bash
sudo apt install python3
```
Wait for the process to complete. Run 
```bash
python3 --version
```
to confirm the installation.

# Step Two (Setting up a Virtual Environment)
## Windows
Go to the Terminal (Windows Powershell) in you preferred project directory and run.
```powershell
python -m venv venv
```
The last venv is the virtual environment name You can choose to call it whatever you want.
Run
```powershell
venv\scripts\activate.bat
```
to activate your environment on windows.
## Linux
Run<br>
```bash
# Start by installing the python venv module 
sudo apt install python3-venv

# In your desired Project directory run
python3 -m venv venv #The last venv can be anything you want

# activate the environment

source venv/bin/activate
```

# Step Three (Cloning the Repository)
On the repo home page click on the dropdown arrow next to the code in _green_ in button and choose clone repository from the dropdown menu.

On you local machine _i.e_ computer go to the terminal and run the following command.

#### Windows
```powershell
git clone https://github.com/Boaz-Maroko/Comic_Book_Reader.git
```
### Linux
```bash
git clone https://github.com/Boaz-Maroko/Comic_Book_Reader.git
```
or

```bash
git clone git@github.com:Boaz-Maroko/Comic_Book_Reader.git
```
if you have **SSH** setup.


# Step Four (Installing dependencies)
## Windows

In windows Terminal (Powershell) run<br>
```powershell
cd comic_book_reader # Change to the project directory

# Then run

pip install -r requirements.txt
```
To install the dependencies from the requirements.txt file.

## Linux
Open the Terminal and run the following command,
```bash
cd comic_book_reader

pip install -r requirements.txt
```
To install the dependencies from the requirements.txt file.


# Bravo
You have successfully set up the project in you local machine. Remember not to distribute the project without my written concent. You can email me [here](mailto:boazmaroko123@gmail.com).

![Enjoy](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbW9jMXFva3MxcDVnZWlkcm43MHV2dWJqaXIydGJiMXNkbXNrNWZ1dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6vXNLzXdW4sbFRGo/giphy.gif)