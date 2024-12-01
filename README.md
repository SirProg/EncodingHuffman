# Compresión y descompresión de imágenes y videos

#### Integrantes grupo 5 - Poyecto de Espol

- Quiroz Vargas Saul Alejandro
- Rocha Vargas Domenica Rafaela
- Espinoza Toala Daniela Joselyn
- Maldonado Paredes Kevin Fernando

#### Para el funcionamiento dentro del entorno virtual
**1.** Inicializa el entorno virtual con el siguiente comando:
`` .venv/Scripts/activate ``
>[!CAUTION] 
>En el caso de que este genere un error, busca el powershell y ábrelo como administrador, luego inserta este código para permitir el funcionamiento del script.
>    `` Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass ``

**2.** Una vez inicializado el entorno virtual en la ruta de tu terminal debe aparecer un (.venv).
Ejemplo: **(.venv)**  _PS C:\Users\NameUser\OneDrive\Documents\proyectName.__
Una vez que se muestre el (.venv) ejecuta el siguiente comando para poder observarlo dentro de tu navegador de confianza.
`` flask --app home run ``
También existe: `` flask --app home --debug run`` te ayudara al momento de realizar cambios y revisar si genera error, por lo cual te dirá en que línea se encuentra.

**3.** Para cerrar el servidor donde se alojo, solo basta con hacer CTRL+C

**4.** Cuando se cierra el servidor y ya no quieras usar el entorno virtual, ejecuta `` deactivate `` en el terminal.


#### Librerías que se está usando dentro del proyecto
- Flask
- Pillow
- OpenCV
- Collections
- Heapq
- Bitarray
- Graphviz