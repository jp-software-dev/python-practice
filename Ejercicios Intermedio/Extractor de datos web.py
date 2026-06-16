import requests
from bs4 import BeautifulSoup

def extraer_precios():
    url = "http://books.toscrape.com"

    try:
        print("Conectando a la tienda de libros...")
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            sopa = BeautifulSoup(respuesta.text, 'html.parser')
            libros = sopa.find_all('article', class_='product_pod')

            print("\nPrimeros 5 libros encontrados:")

            for libro in libros[:5]:
                titulo = libro.h3.a['title']
                precio = libro.find('p', class_='price_color').text

                print(f"Titulo: {titulo}")
                print(f"Precio: {precio}")
                print("---")

        else:
            print(f"Error HTTP. Codigo de estado: {respuesta.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error de red: {e}")

if __name__ == "__main__":
    extraer_precios()