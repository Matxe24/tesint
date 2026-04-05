import os
import subprocess as sub


if os.name == 'nt':
    print("Sorry, This setup is currently only available on Linux. Try using WSL.")
    print("\nIf you are on windows, check out the README.md file or go to the Github page: https://github.com/Matxe24/tesint")
    input()
    exit()

else:
    PATH = input("Enter the path in which you want to put Tesint in: ")
    if os.access(PATH, os.W_OK):
        sub.run("pip -r install requirements.txt", shell = True)
        sub.run(["mv", "tesint.py", PATH])
        newp = f'{PATH}/tesint.py'
        sub.run('python3', newp)
    else:
        print("No write permission. Try running the script with sudo.")
        input()
        exit()
