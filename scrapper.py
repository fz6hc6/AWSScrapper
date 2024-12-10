import requests
from bs4 import BeautifulSoup
import re
import random

l=[]
o={}
specs_arr=[]
specs_obj={}

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
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36']


headers={"User-Agent":useragents[random.randint(0,31)],"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}



product_urls = [
    ("https://www.amazon.es/dp/B0763XM6QC","Groceries"),
        ("https://www.amazon.es/dp/B0CQTM5G4R","Groceries"),
            ("https://www.amazon.es/dp/B07GVQQ1RK","Groceries"),
                ("https://www.amazon.es/dp/B0CH3F9QPJ","Groceries"),
                    ("https://www.amazon.es/dp/B0CJKTWTVT","Televisions & Videos")
    # Añade más URLs de productos si es necesario
]

for target_url, category in product_urls:
    print(f"Procesando: {target_url} - Categoría: {category}")

    resp = requests.get(target_url, headers=headers, proxies=proxies)

#print(resp.text)

    print(resp.status_code)
    if(resp.status_code != 200):
        print(resp)
    soup=BeautifulSoup(resp.text,'html.parser')


    try:
    # Buscar el elemento <span> con id="productTitle"
        title_span = soup.find('span', id='productTitle')

    # Extraer el texto
        if title_span:
            title = title_span.get_text(strip=True)
            #print("Título del producto:", title)
        else:
            print("No se encontró el título del producto.")
    except:
        title=None


#ALL images
#images = re.findall('"hiRes":"(.+?)"', resp.text)
#o["images"]=images

#1 image
#images = soup.find("div",{"class":"imgTagWrapper"})
#o["images"]=images

    try:
    # Buscar el elemento <img>
        img_tag = soup.find('img', class_='a-dynamic-image')

    # Extraer la URL del atributo 'src' y 'data-old-hires'
        if img_tag:
            src_url = img_tag.get('src')
            old_hires_url = img_tag.get('data-old-hires')
            print("URL del atributo 'src':", src_url)
            print("URL del atributo 'data-old-hires':", old_hires_url)
        else:
            print("No se encontró la etiqueta <img>.")
    except:
        src_url=None    
        old_hires_url=None

    #precio actual
    try:
        price=soup.find("span",{"class":"a-price"}).find("span").text
    except:
        price=None


    # Extract the previous price
    try:
        priceold = soup.find('span', {'class': 'a-size-small aok-offscreen'}).text.strip().split(":")[1].strip()

        print("Old Price:", priceold)
    except:
        priceold=None

    # Convertir los precios a números flotantes para el cálculo
    if price:
                    price = price.replace("€", "").strip().replace(".", "").replace(",", ".")
                    #print(str(search_price))

    if priceold:
                    priceold = priceold.replace("€", "").strip().replace(".", "").replace(",", ".")
                    #print(str(product_price_old))
    else:
                    priceold = price

    if float(priceold) != 0:
                    # Calcular el porcentaje de ahorro
                    saving = round(((float(priceold) - float(price)) / float(priceold)) * 100)
                    #print(str(saving))
    else:
                    saving = 0  # Si no hay precios, no se puede calcular el ahorro


    try:
        rating=soup.find("i",{"class":"a-icon-star"}).text
    except:
        rating=None

    #brand model...
    specs = soup.find_all("tr",{"class":"a-spacing-small"})

    for u in range(0,len(specs)):
        spanTags = specs[u].find_all("span")
        specs_obj[spanTags[0].text]=spanTags[1].text.strip()

    specs_arr.append(specs_obj)
    specs_string = " | ".join([f"{key}: {value}" for key, value in specs_obj.items()])

    #specs=specs_arr

    try:
        # Buscar la sección de especificaciones
        feature_bullets = soup.find('div', id='feature-bullets')

        # Extraer las especificaciones
        specifications = []
        if feature_bullets:
            list_items = feature_bullets.find_all('span', class_='a-list-item')
            for item in list_items:
                specifications.append(item.get_text(strip=True))

        # Convertir las especificaciones a una cadena única
        specifications_string = " | ".join(specifications) if specifications else "No se encontraron especificaciones."

        # Imprimir las especificaciones como cadena
        #print("Especificaciones en formato de cadena:")
        #print(specifications_string)
    except:
        specifications_string=None

    specs=specs_string + " " + specifications_string

    # Extract product_id from the URL
    product_id = re.search(r'/dp/([A-Z0-9]{10})', target_url).group(1)
    #print("Product ID:", product_id)

    urlproduct = f"https://www.amazon.es/dp/{product_id}?tag=gangatotal0b-21"


    #print(str(product_id) + str(title) + " " + str(price) + " " + str(priceold) + " " + str(rating) + " " + str(specs))


    # Generate SQL INSERT statement
    insert_sql = f"""
        INSERT INTO productos (merchant_name, aw_product_id, aw_deep_link, merchant_category, 
        product_name, search_price, product_price_old, saving, aw_image_url, description)
        VALUES ('Amazon ES', '{product_id}', '{urlproduct}', 'xxxxxxxxxxxxxx', 
        '{title}', {price}, {priceold}, {saving}, '{src_url}', '{specs}' )
        ON DUPLICATE KEY UPDATE 
        search_price = VALUES(search_price), 
        product_price_old = VALUES(product_price_old), 
        aw_image_url = VALUES(aw_image_url), 
        saving = VALUES(saving);
        """                    

    # Output the generated SQL
    print(insert_sql)
