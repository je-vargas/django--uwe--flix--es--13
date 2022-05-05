<!--: New dependencies that are not included in the dependencies.txt file please add!!! -->
<!--: BY RUNNING:  pip freeze > dependencies.txt -->

# UWEFlix Cinema Booking System - ESD Group 13

## Project Repository Overview
The code is found in the project folder, all other folders are systems and architecture designs.  
The file structure has been designed with good django standards and each application in the project being **films**, **users** and **bookings** have been created to focus on specific resource functionalities.
- All HTML formatting is found inside **templates** which is stored in the root project folder
- **uwe_flix** - Project settings folder

## Branch Control
- **main** branch is used for deployment of working project code that has been checked through pull requests from **development**
- **development** is the most up to date branch and all new features must branch off development for implementation, pull request should be made to development
- **ESD-xx-~~** branches starting with ESD- link to specific tickets found on the jira board, where the number corresponds to the ticket code.
    - All such branches are attached to development and must be merged and tested before being deployed to **main**

## Project Access
Detailed instructions on how to launch the booking system from terminal(cmd).
### File Access
Clone or download zip of the git repo and open in an IDE such as VSCode.
### Virtual Environemnt
Open a new terminal the project space and enter:
#### Windows
```
py -3 -m venv .venv

Set-ExecutionPolicy Unrestricted -Scope Process

.venv\scripts\activate
```
#### MacOS
```
python3 -m venv .venv

source .venv/bin/activate
```
This will create a virtual environemnt to allow us to launch django projects.
### Installing Dependencies
Change directory to the project folder and enter:
```
pip install -r dependencies.txt
```
### Running Migrations
Migrations must also be run from the project directory:
#### Windows
```
python .\manage.py migrate
```
#### MacOS
```
python manage.py migrate
```
### Server Startup
Then to launch the server we can run:
#### Windows
```
python .\manage.py runserver
```
#### MacOS
```
python manage.py runserver
```
Then follow the instructions on the terminal to open the server in a web browser.