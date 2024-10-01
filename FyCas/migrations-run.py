import subprocess
# Ruta al archivo requirements.txt
subprocess.run(["python3", "manage.py", "makemigrations"])
subprocess.run(["python3", "manage.py", "migrate"])
