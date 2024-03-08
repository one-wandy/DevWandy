import subprocess
# Ruta al archivo requirements.txt
path_requirements = "Utils/requirements.txt"
# Ejecutar el comando pip install
subprocess.run(["pip", "freeze", ">", path_requirements ])
