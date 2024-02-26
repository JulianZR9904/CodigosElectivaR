import cv2

# Cargar la imagen del logo del auto
image = cv2.imread('Chevrolet-logo.png')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un umbral
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) # valor del umbral minimo y maximo 

# Encontrar contornos en la imagen umbralizada
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #imagen binaria donde 
                                                                                 #se encuentran los contornos

# hace  una copia de la imagen original incluido todos los pixeles y propiedades para dibujar los contornos
contour_image = image.copy()

# aqui es donde se esta imprimeiendo las coordenadas del contorno que viene de arriba
print(contours)
# Dibujar contornos en la imagen de contornos
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2) # dibuja todos los contornos encontrados en la lista 

# muestra la imagen con contornos

cv2.imshow('Contour Image', contour_image) # muestra imagen en una ventana - titulo de la ventana -imagen 
cv2.waitKey(0)            # espera indefinidamente para poder visulizar la imagen 
cv2.destroyAllWindows()   # cierra todas las ventanas que se allan abierto con la funcion cv2.imshow