import requests
from bs4 import BeautifulSoup
import re
import random
import os

proxies = {
    "http": "http://oqzjnkw:Fz6hc649@http.ntlm.internetpsa.inetpsa.com:8080",
    "https": "http://oqzjnkw:Fz6hc649@http.ntlm.internetpsa.inetpsa.com:8080",
}

useragents=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4894.117 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4855.118 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4892.86 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4854.191 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4859.153 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36/null',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36,gzip(gfe)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4895.86 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4860.89 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4885.173 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4864.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4877.207 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.133 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4872.118 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4876.128 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
     # Chrome User Agents
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.179 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.170 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Safari/537.36",
    # Firefox User Agents
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.0; rv:114.0) Gecko/20100101 Firefox/114.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:112.0) Gecko/20100101 Firefox/112.0",
    # Safari User Agents
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
    "Mozilla/5.0 (iPod touch; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    # Edge User Agents
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36 Edg/117.0.2045.47",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.179 Safari/537.36 Edg/116.0.1938.62",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.170 Safari/537.36 Edg/115.0.1901.204",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36 Edg/114.0.1823.79",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Safari/537.36 Edg/113.0.1774.57",
    # Opera User Agents
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36 OPR/102.0.4880.16",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.179 Safari/537.36 OPR/101.0.4853.20",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.170 Safari/537.36 OPR/100.0.4815.47",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36 OPR/99.0.4788.88",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Safari/537.36 OPR/98.0.4712.99",
    # Mobile User Agents
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.179 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Mi 11 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.170 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Mobile Safari/537.36",
    # Additional User Agents
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 9; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]


headers={"User-Agent":useragents[random.randint(0,31)],"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

product_urls = [
    ("https://www.amazon.es/s?k=iphone&rh=p_n_free_shipping_eligible","Mobiles & Tablets"),
    ("https://www.amazon.es/s?k=television&rh=p_n_free_shipping_eligible","Televisions & Videos"),
    ("https://www.amazon.es/s?k=Samsung&rh=p_n_free_shipping_eligible","Mobiles & Tablets"),
    ("https://www.amazon.es/s?k=Juguetes&rh=p_n_free_shipping_eligible","Toys & Games"),
    ("https://www.amazon.es/s?k=Comida&rh=p_n_free_shipping_eligible","Groceries"),
    ("https://www.amazon.es/s?k=ordernador&rh=p_n_free_shipping_eligible","Computers & Laptops"),
    ("https://www.amazon.es/s?k=decoracion&rh=p_n_free_shipping_eligible","Lighting & Décor"),
    ("https://www.amazon.es/s?k=vestidos&rh=p_n_free_shipping_eligible","Women Fashion"),
    ("https://www.amazon.es/s?k=oficina&rh=p_n_free_shipping_eligible","Furniture & Organization"),
    ("https://www.amazon.es/s?k=belleza&rh=p_n_free_shipping_eligible","Beauty"),
    ("https://www.amazon.es/s?k=videojuegos&rh=p_n_free_shipping_eligible","Electronic & RC Toys"),
    ("https://www.amazon.es/s?k=funko&rh=p_n_free_shipping_eligible","Toys & Games")
    # Añade más URLs de productos si es necesario
]



#url = "https://www.amazon.es/s?k=iphone&rh=p_n_free_shipping_eligible"

# ##################################################################

# # Puedes usar BeautifulSoup para analizar la respuesta cargada
# from bs4 import BeautifulSoup

# if response_content:
#     soup = BeautifulSoup(response_content, "html.parser")
#     # Realiza el análisis deseado
#     print(soup.title.text)
#########################################################


# Abre el archivo en modo append para almacenar los INSERTS
file_path = "inserts.sql"

# def fetch_and_save_response(url, headers, file_path):
#     """
#     Realiza la solicitud a la URL, guarda la respuesta en un archivo.
#     """
#     resp = requests.get(url, headers=headers, proxies=proxies)
#     if resp.status_code == 200:
#         # Guarda el contenido de la respuesta en un archivo
#         with open(file_path, "w", encoding="utf-8") as file:
#             file.write(resp.text)
#         print(f"Respuesta guardada en {file_path}")
#     else:
#         print(f"Error al obtener la respuesta: {resp.status_code}")

# def load_response(file_path):
#     """
#     Carga la respuesta desde el archivo para pruebas.
#     """
#     if os.path.exists(file_path):
#         with open(file_path, "r", encoding="utf-8") as file:
#             response_content = file.read()
#         print(f"Respuesta cargada desde {file_path}")
#         return response_content
#     else:
#         print(f"El archivo {file_path} no existe.")
#         return None

#with open(file_path, "a", encoding="utf-8") as file:
with open(file_path, "w", encoding="utf-8") as file:
    # Itera sobre cada par (URL, categoría) en la lista de productos
    for url, category in product_urls:
        print(f"Procesando: {url} - Categoría: {category}")


    # # # Archivo donde guardar/cargar la respuesta
    # file_path_response = "amazon_response.html"

    # # Usa la función para guardar o cargar
    # if not os.path.exists(file_path_response):
    #     fetch_and_save_response(url, headers, file_path_response)
    # else:
    #     response_content = load_response(file_path_response)

    # if response_content:
    #     soup = BeautifulSoup(response_content, "html.parser")
    # # Realiza el análisis deseado
    #     #print(soup.text)
        
        
        resp = requests.get(url, headers=headers, proxies=proxies)

        print(resp.status_code)
        if(resp.status_code != 200):
            print(resp)
        
        soup=BeautifulSoup(resp.text,'html.parser')

        results = soup.find_all('div', attrs={'data-component-type': 's-search-result'})
 
        result_list = []

        for r in results:
            try:
            # Extrae datos de cada resultado
                title = r.select_one('.a-size-base-plus.a-color-base.a-text-normal')
                price = r.select_one('.a-price .a-offscreen')
                image = r.select_one('.s-image')

                # Extraer precio anterior
                previous_price = r.select_one('.a-price.a-text-price .a-offscreen')
        
                # Extraer valoración
                rating = r.select_one('.a-icon-alt')

                # Extraer ASIN del atributo correspondiente
                asin = r.attrs.get('data-asin')  # Accede directamente al atributo
                urlproduct = f"https://www.amazon.es/dp/{asin}?tag=gangatotal0b-21"


                # Crea un diccionario con los datos extraídos
                result_dict = {
                    "title": title.text.strip() if title else None,

                    "price": price.text.strip() if price else 0,
                    "image": image.attrs['src'] if image else None,
                    "previous_price": previous_price.text.strip() if previous_price else 0,
                    "rating": rating.text.strip() if rating else None,
                    "asin": asin,  # Incluye el ASIN extraído
                    # Añadir la URL al diccionario
                    "urlproduct": urlproduct
                }

                # Añade el diccionario a la lista de resultados
                result_list.append(result_dict)

            except Exception as e:
                # Manejo de errores por si algún elemento no existe o hay problemas
                print(f"Error al procesar un resultado: {e}")

        # Imprime la lista completa de resultados
        #print(result_list)

        #Leemos el diccionario:
        # Supongamos que result_list es tu lista de diccionarios con los productos
        for product in result_list:
            try:
                # Obtener los valores del diccionario
                merchant_name = "Amazon ES"
                aw_product_id = product.get("asin")
                aw_deep_link = product.get("urlproduct")
                merchant_category = "telefonia"
                product_name = product.get("title").replace("'","")
                search_price = product.get("price")
                product_price_old = product.get("previous_price")
                aw_image_url = product.get("image")

                print(product_name + " " + str(search_price) + " " + str(product_price_old))


                # Convertir los precios a números flotantes para el cálculo
                if search_price:
                    search_price = search_price.replace("€", "").strip().replace(".", "").replace(",", ".")
                    #print(str(search_price))

                if product_price_old:
                    product_price_old = product_price_old.replace("€", "").strip().replace(".", "").replace(",", ".")
                    #print(str(product_price_old))
                else:
                    product_price_old = search_price

                if float(product_price_old) != 0:
                    # Calcular el porcentaje de ahorro
                    saving = round(((float(product_price_old) - float(search_price)) / float(product_price_old)) * 100)
                    #print(str(saving))
                else:
                    saving = 0  # Si no hay precios, no se puede calcular el ahorro

                print(product_name + " " + str(search_price) + " " + str(product_price_old))

                if float(search_price) != 0:
                # Generar el SQL INSERT con ON DUPLICATE KEY UPDATE
                    insert_sql = f"""
                    INSERT INTO productos (merchant_name, aw_product_id, aw_deep_link, merchant_category, 
                    product_name, search_price, product_price_old, saving, aw_image_url)
                    VALUES ('{merchant_name}', '{aw_product_id}', '{aw_deep_link}', '{category}', 
                    '{product_name}', {search_price}, {product_price_old}, {saving}, '{aw_image_url}')
                    ON DUPLICATE KEY UPDATE 
                    search_price = VALUES(search_price), 
                    product_price_old = VALUES(product_price_old), 
                    aw_image_url = VALUES(aw_image_url), 
                    saving = VALUES(saving);
                    """
            
                # Escribir el INSERT en el archivo
                file.write(insert_sql + "\n")
            except Exception as e:
                print(f"Error al generar el insert para el producto {product.get('title')}: {e}")