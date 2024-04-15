import nltk
import requests
from bs4 import BeautifulSoup

# Función para extraer texto de una página web
def extraer_texto(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        texto = soup.get_text()
        return texto
    else:
        print("Error al obtener la página:", response.status_code)
        return None

# URL de la página web que deseas analizar
url_pagina = str(input("Ingresa la url a analizar: \n"))
texto_pagina = extraer_texto(url_pagina)

# Guardar el texto extraído en un archivo de texto
if texto_pagina:
    with open("texto_pagina.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto_pagina)

# Cargar el texto del archivo
archivo_nombre = "texto_pagina.txt"
with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

print("----------------------------------------------------------------------")

# Cargar palabras funcionales en español de NLTK
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
    print(palabras_funcional)

print("----------------------------------------------------------------------")

# Tokenizar el texto y eliminar palabras funcionales
tokens = nltk.word_tokenize(texto, "spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print(tokens_limpios)
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

# Graficar las 40 palabras más comunes
distribucion_limpia.plot(40)