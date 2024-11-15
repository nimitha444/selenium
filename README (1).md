# selenium
Description

Automated testing using selenium library.
Git commands and other commands used in command prompt:

    mkdir <file_name> to create the folder
    cd <file name> to go inside the folder
    git init, initializing folder as git repository
    git add . to add all the files into git track
    git commit -m "<message>", it commits whatever is there in the track
    git remote add origin <GitHub repository link>, builds connection between git and github
    git push --set-upstream origin master, sends all the files from git to github
    pip install selenium to install selenium

Steps:

    Create a new item under Freestyle Project item type
    Select Git in Source Code Management
    Add Execute Windows Batch Command step in Build Steps
    Save the configurations
    Build now and visualize console output
    Install selenium in the command prompt using the command mentioned above
    Execute the selenium python code
    After successful execution of the code, google chrome browser should automatically open and quit itself

