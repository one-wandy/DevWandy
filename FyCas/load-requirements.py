import subprocess

# Ruta al archivo requirements.txt
path_requirements = "Utils/requirements.txt"

# Ejecutar el comando pip freeze y redirigir la salida al archivo
with open(path_requirements, "w") as f:
    subprocess.run(["pip", "freeze"], stdout=f)
