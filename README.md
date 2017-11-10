# Prerequisites

Log in to the repo server before using the automation. This will prevent issues involving ssh authentication, 
as the script is not written to perform a first time setup of the ssh connection.
  
## SSH Keys
To use this program, you need to set up SSH keys with the repo server.
To do this, go to a terminal, and enter: 
 ssh-keygen
This will generate an authentication key for your ssh instance.
From there, copy the key to the repo server.
 ssh-copy-id username@127.0.0.1
with username as a placeholder for the repo username, 
and 127.0.0.1 as a placeholder for the repo server IP.
    
## Resetting Constants
There are some constants that you may want to update. Mainly the BUGZILLA_URL and 
DEFAULT_PASSWORD. This is if you want to change either the url to get to 
bugzilla, or the default password given to the new hires accounts. BUGZILLA_URL and
DEFAULT_PASSWORD can be found in account_automation.py.

## Gmail Authentication
To setup gmail authentication, follow the steps in the following link
(Note: The quickstart file can be found in the email_notification subfolder. Ensure it's 
run while your working directory is the root of the account_automation project.) 
 [Gmail Authentication](https://developers.google.com/gmail/api/quickstart/python) 
The client_secret.json should be placed in the root of the project. 
    
## Setup Scripts
The setup scripts will do most of the work required before running the
automation. However, assuming you follow the order of this wiki, the scripts will perform the final steps.
This installs most of the dependencies and updates what is needed.
Each step will: 
 - install expect
 - update firefox
 - install pip
 - install selenium for python
 - install geckodriver for selenium interaction with firefox
 - install gmail python api client.
To run this script, go into the setup folder and enter:
 sudo bash init.sh apt-get
This assumes that you are using an operating system with apt as the package manager. ''init.sh''
will run all the other scripts in the folder, but if you only need one of those, you can just use
the one by itself.

# Running account_automation

## Without Arguments

To run account_automation, simply go to the root directory and enter 
 python account_automation.py
in the terminal. This should give you a list of prompts for
the necessary details to automate the account creation. 
The details requested are: 
 - the name of the new hire
 - the email of the new hire
 - whether or not the new user is a developer
 - the bugzilla login of the admin 
 - the bugzilla password of the admin
 - the IP address of the repo server (127.0.0.1)
 - the admin username on the repo server (root)
 - the password for the admin of the repo server

## With Arguments
'''A table with the list of arguments is at the end of this section.'''

An example usage of some of the command line arguments would be as follows:
 python account_automation.py -n "Forename Surname" -e "forename.surname@<<company-name>>.com" -a "admin@<<company_name>>.com" -r "127.0.0.1" -u "root"
The prompts left after this command would request:
 - If the new hire is a developer
 - Password for the 'admin@<<company-name>>.com' bugzilla account
 
Adding a -d would reduce it to just the bugzilla password, assuming the new user is a developer.


### Command Line Arguments
|Short |Long            |Function                                       |
|:----:|:--------------:|:----------------------------------------------|
|-a    |--adminemail    |Email address for the automator                |
|-d    |--dev           |If the new user is a developer, add this.      |
|-e    |--email         |Email address of the new hire                  |
|-h    |--help          |show this help message and exit                |
|-n    |--name          |Name of the new hire                           |
|-r    |--reposerver    |Repo Server domain (e.g. ssh fs@<reposerver>)  |
|-s    |--sshpassword   |Use password with SSH as keys are not set up   |
|-u    |--adminusername |Admin username on the repo server              |
