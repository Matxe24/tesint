import subprocess as sub
import os

if os.name == 'nt':
    try:
        sub.run('py -m pip install -r requirements.txt', shell=True, check=True)
        print("Configuration finished.")
        input()
    except Exception:
        print("Configuration failed, try running 'py -m pip install -r requirements.txt' in Powershell.")
        input()
        exit()
else:
    print("This is only for windows. Check out the README or the github page on https://github.com/Matxe24/tesint for the installation for your specific platform")
    input()
    exit()
