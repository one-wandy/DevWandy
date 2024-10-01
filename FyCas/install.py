
import os
import sys
import subprocess

path = os.getcwd() + "\env"
def CreateEnv(ruta):
    try:
        # Crear el entorno virtual
      subprocess.run([sys.executable, "-m", "venv", path])
      print("Entorno Virtual Creado Correctamente")


# Ejecutar el script de activación
   
    except Exception as e:
        print(f"Error al crear el entorno virtual: {e}")

if __name__ == "__main__":
      if not os.path.exists(path):
            os.makedirs(path)
      CreateEnv(path)
      path_env = os.getcwd() + "\env\Scripts"
      activate_script = os.path.join(path_env, "activate.bat") if os.name == "nt" else os.path.join(path_env, "activate")
      subprocess.run([activate_script], check=True)
      if sys.prefix:
             print("Entorno virtual activo:", sys.prefix)
      else:
            print("No hay un entorno virtual activo")
