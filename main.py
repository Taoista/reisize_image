# 
# software que cambia el tamano de la imagen
# 
# 
# 
import os
import shutil
from PIL import Image

def create_folder_start():
    folder_name = "inicio"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return os.path.abspath(folder_name)

def create_folder_finish():
    folder_name = "finish"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return os.path.abspath(folder_name)

def resize_and_copy_images(src_folder, dest_folder, new_width, new_height):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    for filename in os.listdir(src_folder):
        if filename.endswith((".jpg", ".png", ".jpeg")):  # Añade aquí otros formatos de imagen si es necesario
            image = Image.open(os.path.join(src_folder, filename))
            image_resized = image.resize((new_width, new_height))
            
            # Guarda la imagen redimensionada en la carpeta de destino con el mismo nombre de archivo
            image_resized.save(os.path.join(dest_folder, filename))

def  main():
    # ? crea el ruta de la imagenes
    path = create_folder_start()
    path_finisht = create_folder_finish()
    width = 1500
    height = 1500    

    resize_and_copy_images(path, path_finisht,width,height)


if __name__ == "__main__":
    main()
