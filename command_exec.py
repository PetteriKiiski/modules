import subprocess
print (str().join(subprocess.check_output(["clear"]).decode("UTF-8").split("\n")[0:-2]))
