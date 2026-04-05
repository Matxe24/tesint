# TESINT
Tesint is an open source osint tool that aims to be the best one before 2030. It has various modules, even though it's not even close to finished yet.
It's a solo project and i'm constantly working on it, trying to give y'all a good experience and possibly walk more and more people into the world of OSINT(crypto donations will be open as soon as i finish the whole tool, because i'm not here begging for money. The way you can support me is by using this tool, it makes me so happy knowing someone uses it).

We are going to start off with the installation process on various platforms, how to update on various platforms and what each module does.

DISCLAIMER: This tool REQUIRES python and git to be installed on your device.

RUNNING TIP: Since this tool has a big ASCII banner at the start, i reccomend using fullscreen or you will have trouble reading modules.

# LINUX

Open a terminal and clone the repository by typing 'git clone https://github.com/Matxe24/tesint'. After that, go in that directory by running 'cd tesint' and run the setup.py by typing 'python3 setup.py'. It will install the required modules and then move out the tool to a directory that you want.
If you want to open the tool each time you type 'tesint' in your terminal, no matter what directory you're in, then do this simple process:
Open the python file and on top of everything write: #!/usr/bin/python3. Then rename the file 'tesint' removing the .py extention. After that, run this command:'chmod +x tesint'(if it gives you an error try using sudo with it, doing 'sudo chmod +x tesint' that will ask you for your password to continue). Then just run 'sudo mv tesint /usr/local/bin'(it will ask for the sudo password since it's a privileged command, unless you're using root) and your installation is complete, just close and reopen your terminal and then whenever you type in 'tesint' it will open.

# WINDOWS

Firstly install Git(you can watch a tutorial on youtube.). Once it's installed, open Powershell and run this command(from the first #-- all over to the last #--:

#--

cd $HOME\Desktop

git clone https://github.com/Matxe24/tesint

cd tesint

py py_conf.py

#--

After it's finished cloning you don't need to run the setup file, instead, go in your desktop and find the folder 'tesint'. Open it and move tesint.py wherever you want. To run it, just double click on it.

# MACOS

MacOS is currently untested, but it should work similarly to linux. Tips are welcome.

# UPDATING

When an update occurs the tool warns you about it, here is how to update on different platforms.

# LINUX

On linux you really don't have to do anything, because the tool will give you the option to update: if you select yes, the update will be automated, you just have to enter the path in which you want the tool to be in. If you want the automatic tesint start when you enter "tesint" in the terminal, just do what you did in the installation again.

# WINDOWS

When the tool gives you the option DON'T SELECT YES, instead, delete the old tesint folder and files and do the installation process all over again.

# MacOS

Same thing as before.

# ALL THE MODULES

Right now there are so few modules, so i will not be covering up to them. When there will be a lot of modules i will explain how each works.

# ENJOY THE TOOL!
