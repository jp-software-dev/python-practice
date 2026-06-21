# 'requests' nos permite descargar el codigo de la pagina web (hacer peticiones HTTP)
import requests
# 'BeautifulSoup' nos ayuda a navegar por el HTML y buscar etiquetas especificas facilmente
from bs4 import BeautifulSoup

def extraer_precios():
    # URL de una tienda de libros de prueba para Web Scraping
    url = "http://books.toscrape.com/"
    
    try:
        print(f"Conectando a {url}...\n")
        # Descargamos todo el contenido de la pagina web
        respuesta = requests.get(url)
        # Verificamos que la pagina haya cargado correctamente (codigo 200 OK)
        respuesta.raise_for_status()
        
        # Le pasamos el texto HTML a BeautifulSoup para que lo convierta en un objeto estructurado
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        
        # Buscamos TODOS los contenedores (articulos) que tengan la clase 'product_pod'
        # Sabemos esto porque inspeccionamos el codigo fuente de la pagina previamente con el navegador
        libros = soup.find_all('article', class_='product_pod')
        
        # Imprimimos la cabecera de nuestra tabla visual
        print("-" * 50)
        print(f"{'TITULO DEL LIBRO':<35} | {'PRECIO':<10}")
        print("-" * 50)
        
        # Iteramos (recorremos) cada uno de los libros que encontro en la pagina
        for libro in libros:
            # El titulo real esta oculto en el atributo 'title' dentro de la etiqueta <a> dentro del <h3>
            titulo = libro.h3.a['title']
            
            # El precio esta dentro de un parrafo <p> que tiene la clase 'price_color'
            # .text extrae solo las letras/numeros, ignorando las etiquetas HTML
            precio = libro.find('p', class_='price_color').text
            
            # Si el titulo es muy largo, lo recortamos y le ponemos "..." para que no rompa nuestra tabla
            if len(titulo) > 32:
                titulo = titulo[:29] + "..."
                
            # Imprimimos la fila alineando el titulo a la izquierda con 35 espacios (<35)
            print(f"{titulo:<35} | {precio:<10}")
            
        print("-" * 50)
        print(f"[+] Se extrajeron {len(libros)} articulos exitosamente.")
        
    except requests.exceptions.RequestException as e:
        # Capturamos cualquier error de conexion (sin internet, pagina caida, etc.)
        print(f"[-] Error de red al intentar conectar con la pagina: {e}")

# Punto de entrada estandar
if __name__ == "__main__":
    extraer_precios()