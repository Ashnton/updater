import subprocess
subprocess.call(["sudo", "apt", "update", "-y"])
subprocess.call(["sudo", "apt", "upgrade", "-y"])
subprocess.call(["sudo", "apt", "full-upgrade", "-y"])
subprocess.call(["sudo", "apt", "dist-upgrade", "-y"])
subprocess.call(["sudo", "apt", "autoremove", "-y"])
subprocess.call(["exit"])



