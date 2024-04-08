import requests
idusr = input('Introduce ID de usuario: ')
url = f"https://www.habbo-happy.net/me/mensajes/{idusr}"
headers = {
    "Host": "www.habbo-happy.net",
    "Cookie": "PHPSESSID=165b29b5980da1553171bcfe2e80d86d; cookies=true; _ga_G1NN29BXC6=GS1.1.1712533411.3.1.1712540253.0.0.0; _ga=GA1.1.884789876.1712523082; __eoi=ID=1290dfaa789b83a7:T=1712523119:RT=1712540062:S=AA-Afjagvd6esLM1eZFtJaRdDJry; browsertoken=ca33d5e440a8a126d22e54366b2ceaecac94e76a",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "55",
    "Origin": "https://www.habbo-happy.net",
    "Referer": "https://www.habbo-happy.net/me/mensajes/51104",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Te": "trailers"
}
data = {
    "replyconversation": "BotSpammer By Aforak",
    "sendreplyconversation": "Enviar"
}

num_requests = 1000  # Cambia esto al número de solicitudes que quieres enviar

for i in range(num_requests):
    response = requests.post(url, headers=headers, data=data)
    print(f"Request {i+1}:")
    print('OK')
    print("------------------------")
