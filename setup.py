import os
import subprocess as sub
import sys

if os.name == 'nt':
    print("Sorry, This setup is currently only available on Linux. Try using WSL.")
    print("\nIf you are on windows, check out the README.md file or go to the Github page: https://github.com/Matxe24/tesint")
    input()
    exit()

else:
    PATH = input("Enter the path in which you want to put Tesint in: ")
    if os.access(PATH, os.W_OK):
        try:
            sub.run(
                [sys.executable, "-m", "pip", "install", "--user", "-r", "requirements.txt"],
                check=True,
                stdout=sub.DEVNULL,
                stderr=sub.DEVNULL
            )
        except Exception:
            sub.run(
                [sys.executable, "-m", "pip", "install", "--user", "-r", "requirements.txt", "--break-system-packages"],
                check=True,
                stdout=sub.DEVNULL,
                stderr=sub.DEVNULL
            )

        target_path = os.path.join(PATH, "tesint.py")
        os.rename("tesint.py", target_path)
        os.chmod(target_path, 0o755)
        sub.run([sys.executable, target_path])

    else:
        print("No write permission. Try running the script with sudo.")
        input()
        exit()
