Script para preparar la maquina update upgrade y pip.

#!/bin/bash

# Actualización de la lista de paquetes
sudo apt-get update -y

# Actualización de los paquetes instalados
sudo apt-get upgrade -y

# Instalación de pip3
sudo apt-get install python3-pip

# Clonando el repo
#git clone https://github.com/joanroamora/langChainProject.git

# Mensaje de finalización
echo "**Actualización y instalación completadas**"