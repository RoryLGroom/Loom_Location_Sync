# To install , first create a virtual environment, using the python command

python -m venv .venv

You can replace ".venv" with any name you wish for your virtual environment folder

## Then to activate, depending on your platform, run command 
------------------------------------------------------------------------------------

### POSIX

bash/zsh

$ source <venv>/bin/activate

fish

$ source <venv>/bin/activate.fish

csh/tcsh

$ source <venv>/bin/activate.csh

pwsh

$ <venv>/bin/Activate.ps1

### Windows

cmd.exe

C:\> <venv>\Scripts\activate.bat

PowerShell

PS C:\> <venv>\Scripts\Activate.ps1

## After virtual environment is created and activated, install dependencies by using command 

pip install -r requirements.txt

# Using Hologram API 
create a seperate file in root directory called .env, and add a file called config.py. 

In this file, add a variable called MY_API_KEY, and assign it the value of the hologram API key. 

Ex. MY_API_KEY = "secret_key_here"