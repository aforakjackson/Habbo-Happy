import requests

# Obtén el mensaje del usuario
msg_input = input("Introduce tu mensaje: ")

# Obtén el número de veces que se enviará la solicitud
num_requests = int(input("Introduce el número de veces que se enviará la solicitud: "))

url = "https://www.habbo-happy.net/chat/process"
headers = {
    "Host": "www.habbo-happy.net",
    "Cookie": "PHPSESSID=165b29b5980da1553171bcfe2e80d86d; cookies=true; _ga_G1NN29BXC6=GS1.1.1712533411.3.1.1712541963.0.0.0; _ga=GA1.1.884789876.1712523082; __eoi=ID=1290dfaa789b83a7:T=1712523119:RT=1712541681:S=AA-Afjagvd6esLM1eZFtJaRdDJry; browsertoken=ca33d5e440a8a126d22e54366b2ceaecac94e76a",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "*/*",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "11",
    "Origin": "https://www.habbo-happy.net",
    "Referer": "https://www.habbo-happy.net/comunidad",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers"
}
data = {"msg": msg_input}

# Envía la solicitud el número de veces especificado
for i in range(num_requests):
    response = requests.post(url, headers=headers, data=data)
    print(f"Solicitud {i+1}:")
    print(response.status_code)
    print(response.text)
    print("--------------")
