# Gestionar paquetes

**Intalar paquetes**

- pip install requests

**Listar paquetes instalados**

- pip list

**Instalar versión especificada**

- pip install requests==2.18.1

- pip install requests==2.18.*

- pip install requests==2.*

**Instalar la versión más parecida**

- pip install requests~=2.18.1

# Ambiente Virtual

**Crear ambiente virtual**

- python -m venv env

**Activar ambiente virtual**

- env/Scripts/activate

- Activando el ambiente virtual puede que lance un error de seguridad, para poder ejecutarlo usar el siguiente código `Set-ExecutionPolicy Unrestricted -Scope Process` y posteriormente ejecutar el activate

**Desactivar ambiente virtual**

- deactivate

# pipenv

**Instalar pipenv**

- pip install pipenv

**Instalar paquetes**

- pipenv install requests

**Activar ambiente virtual**

- pipenv shell

**Desactivar ambiente virtual**

- exit

**Instalar paquetes desde pipfile**

- pipenv install

**Instalar paquetes desde pipfile.lock**

- pipenv install --ignore-pipfile

**Actualizar paquetes desactualizados**

- pipenv update --outdated

**Actualizar todos los paquetes**

- pipenv update
