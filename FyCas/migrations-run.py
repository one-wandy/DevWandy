import subprocess
# Ruta al archivo requirements.txt
subprocess.run(["py", "manage.py", "makemigrations"])
subprocess.run(["py", "manage.py", "migrate"])
