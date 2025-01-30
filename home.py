from flask import Flask, render_template, url_for, request, redirect
from collections import Counter
from werkzeug.utils import secure_filename
from PIL import Image
import os
from images_manipulation import compress_image, descompress_image

app = Flask(__name__)

#Creación de los directorios en caso de que no existan, con ello la función ensure_dic
app.config['UPLOAD_FOLDER'] = 'upload'
app.config['COMPRESSED_FOLDER'] = 'compress'
app.config['DESCOMPRESSED_FOLDER'] = 'descompress'

def ensure_dic(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

ensure_dic(app.config['UPLOAD_FOLDER'])
ensure_dic(app.config['COMPRESSED_FOLDER'])
ensure_dic(app.config['DESCOMPRESSED_FOLDER'])

#Inicio de la página
@app.route("/")
def home():
    return render_template('index.html', )

# UPLOAD FILES  
@app.route('/upload', methods = ['POST'])
def upload():
    #Manejo de subida de archivos solo para imagenes
    if 'inputFile' not in request.files:
        error = "Key not found"
        return render_template('index.html', error = error)
    file = request.files['inputFile']
    if file.filename == "":
        error = "No content filename or filename not exist"
        return render_template('index.html', error = error)
    file_type = file.content_type.split("/")[0]
    #Verifica que es un archivo de tipo imagen
    if file and file_type == "image":
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(original_path)
        file_data = file.filename.split('.')
        # Abre la imagen y comienza el proceso de comprensión
        with Image.open(original_path) as img:
            compress_data = compress_image.compress_image_func(img)

        # Se comprime en su totalidad y se guarda los datos en las carpetas
        compress_filename = f"compressed_{file_data[0]}.{file_data[-1]}"
        compress_path = os.path.join(app.config['COMPRESSED_FOLDER'], compress_filename)
        with open(compress_path, 'wb') as f:
            compress_data['encode_data'].tofile(f)

        # Se descomprime usando los datos de la imagen comprimida y este se guarda como una imagen.
        descompress_img = descompress_image.descompress_image_func(compress_data)
        descompress_path = os.path.join(app.config['DESCOMPRESSED_FOLDER'], f"descompress_{file.filename}")
        descompress_img.save(descompress_path)

        # Calculo para ver las estadisticas de la imagen original y la descomprimida
        original_size = os.path.getsize(original_path)
        compress_size = os.path.getsize(descompress_path)
        compress_ratio = (1-(compress_size/original_size)) * 100

        #renderiza o carga el template index.html llevando los datos como parametros.
        return render_template('index.html',
                original_size = original_size,
                compress_size = compress_size,
                compress_ratio = f"{compress_ratio:.2f}",
                compress_image_url = descompress_path)

    return render_template('index.html')


# ERROR FILES

@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'),404

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('error/405.html'), 405