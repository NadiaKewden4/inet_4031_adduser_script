# INET4031 Add Users Script and User List

## Program Description
This program will help the user in doing more than manual commands. In the script everything is set up for the user such creating users, passwords and the specific groups. This automated way of doing things is simple and helps the user not run into errors. The commands used to add a user were are useradd, passwd and groupadd and the script uses these same ones but it automates and works behind close doors, we just don't see it visually.

## Program User Operation
The overall operation of the program, uses an automated script and each line of the script has all the information needed to add a user. Once the file is set you can run it and it will display prompt commands based on the python code and all of this will be done automatically without needing any manual input. 

## Input File Format
The format was done in a file and edited in nano, to create a user the input file will need the user, password, and group name. These are all important in ensuring that everything works as expected.

## Command Execution 
To run the code terminal must be open and the user might need to set the python file to be executable, ./create-users.py < createusers.input.

## "Dry Run"
If the user chooses to do a "dry run" the commands from the script won't follow thorugh, but what will happen is it will print out the commands that should've been executed.
