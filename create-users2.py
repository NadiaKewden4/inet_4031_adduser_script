#!/usr/bin/python3

# INET4031
# Nadia Kewden
# 3/25/25
# 3/25/25


#The first os import allows for commands to be ran.
#The second re import is for checking similiar regular expressions.
#The third sys import signals for command lines to do what is expected.
import os
import re
import sys

#From my understanding dry run shows you the outputs of the commands you put without running them, however in my case I should've got printed comands but I didn't which is something i'm confused about?

def main():
    answer = input("Need to dry run? Type Y to dry run or N to run code normally: ")
    for line in sys.stdin:
        #This line signals that if "#" exists it should skip because it's a comment, this ensures that the code runs successfully without any errors.
        match = re.match("^#",line)

        #This line indicates that when ":" is used it allows the line of code to split into different parts.
        fields = line.strip().split(':')

        #The IF statement shows that if a line or a field doesn't have at least 5 lines of information then skip it and continue.
        #IF statement is checking for if it's a match.
        #IF the the statement is true it skips the line and continues to the next one.
        if match or len(fields) != 5:
            if answer == 'N':
                print("dry run skips line (needs more information or lines)")
            continue

        #The purpose of these lines get the username and password information of the users.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This split is being done to ensure that the groups don't get mixed up and to ensure that there isn't more than one group for a user.
        groups = fields[4].split(',')

        #The print statement indicates what account is being created for the user.
        print("==> Creating account for %s..." % (username))
        #This allows for a user to be added without the user needing a password (disables passowrd).
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        if answer == 'N':
            print("Dry run - will run:", cmd)
        else:
            os.system(cmd)

        #This print statement shows when the password is set for the user.
        print("==> Setting the password for %s..." % (username))
        #The line is running the password twice, and the "cmd" contains the command line to run in the terminal.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        if answer == 'N':
            print("Dry run - will run:", cmd)
        else:
            os.system(cmd)

        for group in groups:
            #If there there is a known group with not only equals to "-" then continue to add that user to the group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
        if answer == 'N':
            print("Dry run - will run:", cmd)
        else:
            os.system(cmd)

if __name__ == '__main__':
    main()
