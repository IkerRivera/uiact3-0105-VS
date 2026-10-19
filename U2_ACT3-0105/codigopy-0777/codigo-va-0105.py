
import cv2
import matplotlib.pyplot as plt
import os
#Iker Montoya 
# Definir rutas
carpeta_proyecto = os.path.dirname(os.path.abspath(__file__))
carpeta_principal = os.path.dirname(carpeta_proyecto)

ruta_imagen = os.path.join(carpeta_principal, "img-original-0105", "Plancha.jpg")
carpeta_resultados = os.path.join(carpeta_principal, "resultados")

# Crear carpeta resultados
os.makedirs(carpeta_resultados, exist_ok=True)

# Cargar imagen
img = cv2.imread(ruta_imagen)

if img is None:
    print("Error: no se encontro Plancha.jpg")
    print("Ruta buscada:", ruta_imagen)
    exit()

# Convertir de BGR a RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Separar canales
R, G, B = cv2.split(img)

# Mostrar canales
fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(R, cmap="gray")
ax1.set_title("CANAL ROJO")

ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(G, cmap="gray")
ax2.set_title("CANAL VERDE")

ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(B, cmap="gray")
ax3.set_title("CANAL AZUL")

# Reconstruir imagen
imgre = cv2.merge((R, G, B))

ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")

plt.tight_layout()

# Guardar resultado
ruta_salida = os.path.join(carpeta_resultados, "Plancha_canales.png")
plt.savefig(ruta_salida)

print("Imagen guardada en:", ruta_salida)

plt.show()
print("Iker Montoya 0105")