import subprocess as sub
import os

if os.name == 'nt':
    try:
        sub.run('py -m pip install -r requirements.txt')
        input()
        print("Configuration finished.")
    except any:
        print("Configuration failed, try running 'py -m pip install -r requirements.txt' in Powershell.")
        input()
        exit()
