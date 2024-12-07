import os
from PIL import Image

# Ruta de la carpeta con las imágenes
ruta_carpeta = "train"
nueva_carpeta = "emotions_resized"

# Crear la nueva carpeta si no existe
if not os.path.exists(nueva_carpeta):
    os.makedirs(nueva_carpeta)

# Recorrer subcarpetas
for subcarpeta in os.listdir(ruta_carpeta):
    ruta_subcarpeta = os.path.join(ruta_carpeta, subcarpeta)

    # Verificar si es una carpeta
    if os.path.isdir(ruta_subcarpeta):
        # Crear una subcarpeta equivalente en la carpeta de salida
        nueva_subcarpeta = os.path.join(nueva_carpeta, subcarpeta)
        if not os.path.exists(nueva_subcarpeta):
            os.makedirs(nueva_subcarpeta)
        
        # Procesar imágenes en la subcarpeta
        for archivo in os.listdir(ruta_subcarpeta):
            if archivo.endswith((".png", ".jpg", ".jpeg")):  # Ajusta las extensiones según tus imágenes
                ruta_imagen = os.path.join(ruta_subcarpeta, archivo)
                imagen = Image.open(ruta_imagen)
                imagen_redimensionada = imagen.resize((32, 32), Image.Resampling.LANCZOS)
                
                # Guardar la imagen redimensionada en la subcarpeta de salida
                ruta_nueva_imagen = os.path.join(nueva_subcarpeta, archivo)
                imagen_redimensionada.save(ruta_nueva_imagen)

print(f"Imágenes redimensionadas guardadas en: {nueva_carpeta}")
