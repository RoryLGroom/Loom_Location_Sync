# Setup and Installation
## Create a Virtual Environment

Create a virtual environment using:

python -m venv .venv

You may replace .venv with any folder name of your choice.

## Activate the Virtual Environment

Activation depends on your operating system and shell.

macOS / Linux (POSIX)

bash / zsh

source <venv>/bin/activate

fish

source <venv>/bin/activate.fish

csh / tcsh

source <venv>/bin/activate.csh

PowerShell (pwsh)

<venv>/bin/Activate.ps1
Windows

Command Prompt (cmd.exe)

<venv>\Scripts\activate.bat

PowerShell

<venv>\Scripts\Activate.ps1

Replace <venv> with the name of your virtual environment folder (e.g., .venv).

## Install Dependencies

Once the virtual environment is activated, install required packages:

pip install -r requirements.txt
Hologram API Configuration

To use the Hologram API, create a configuration file to store your credentials.

### Create Configuration File

In the root directory of the project, create a file named:

config.py
### Add Your API Key

Inside config.py, define your API key:

hologram_api_key = "your_hologram_api_key_here"

Replace "your_hologram_api_key_here" with your actual Hologram API key.

### Security Note

Do not commit config.py to version control.
Add it to your .gitignore file to prevent exposing your API credentials.

Example .gitignore entry:

config.py

# Documentation and Demo Video
### Demo Video
<link> https://youtu.be/SPvb7UfcVZg </link>

### Documentation 
<link> https://docs.google.com/document/d/1iaowcdVThSG-IY-LXu3ZF7BfUnMEFDJIBt4f9tBCXrU/edit?usp=sharing </link>
