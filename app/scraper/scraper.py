# Scraper logic placeholder
import requests
from bs4 import BeautifulSoup
WISE_URL = "https://wise.com/es/currency-converter/usd-to-pen-rate?amount=1" # para un dolar
KAMBISTA_URL = "https://kambista.com/?utm_source=google&utm_medium=cpc&utm_campaign=max_rendimiento&utm_content=inversionistas&gad_source=1&gad_campaignid=22614168948&gbraid=0AAAAABndTR0BP90hbvD-w2KGsnFyPzEAo&gclid=CjwKCAjw2vTFBhAuEiwAFaScwlojR4LIQAJn1RRjsoFa18nbagocEPzzOd9Hsd43FkW-pfl7umaWBBoCZbgQAvD_BwE"
SECUREX_URL = "https://securex.pe/"#todo

def scrape(url: str):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.prettify()  # Retorna todo el HTML formateado
    else:
        return f"Error: Código de estado {r.status_code}"
    
def extract_dolar_value_wise(html: str) -> float:
    soup = BeautifulSoup(html, "html.parser")
    rate_input = soup.find(id="target-input")
    if rate_input and rate_input.has_attr("value"):
        rate_text = rate_input["value"].strip().replace(",", ".")
        try:
            return float(rate_text)
        except ValueError:
            raise ValueError(f"No se pudo convertir el valor a float: {rate_text}")
    else:
        raise ValueError("No se encontró el input con id 'target-input' o no tiene atributo 'value'.")

#TODO : hacer con selenium
def extract_dolar_value_google(html: str) -> float:
    soup = BeautifulSoup(html, "html.parser")
    # Buscar el span usando el id y la estructura del xpath
    container = soup.find(id="knowledge-currency__updatable-data-column")
    if container:
        try:
            valor_span = container.select_one("div:nth-of-type(1) > div:nth-of-type(2) > span:nth-of-type(1)")
            if valor_span:
                valor_text = valor_span.text.strip()
                return float(valor_text)
            else:
                raise ValueError("No se encontró el span con el valor del dólar.")
        except Exception as e:
            raise ValueError(f"Error al extraer el valor: {e}")
    else:
        raise ValueError("No se encontró el contenedor con id 'knowledge-currency__updatable-data-column'.")

def extract_dolar_value_kambista(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    compra = soup.find(id="valcompra")
    venta = soup.find(id="valventa")
    if compra and venta:
        try:
            valor_compra = float(compra.text.strip())
            valor_venta = float(venta.text.strip())
            return {"compra": valor_compra, "venta": valor_venta}
        except Exception as e:
            raise ValueError(f"Error al extraer los valores: {e}")
    else:
        raise ValueError("No se encontraron los elementos con id 'valcompra' y/o 'valventa'.")
    
#def extract_dolar_value_securex(html: str) -> dict:

body=scrape(SECUREX_URL)
print(body)
#print(extract_dolar_value_google(body))
#print(extract_dolar_value(body))
