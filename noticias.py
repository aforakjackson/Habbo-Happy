import requests
urlnoti = input('Introduce URL de la noticia de Habbo-Happy: ')
url = f"{urlnoti}"
headers = {
    "Cookie": "PHPSESSID=165b29b5980da1553171bcfe2e80d86d; cookies=true; _ga_G1NN29BXC6=GS1.1.1712533411.3.1.1712533489.0.0.0; _ga=GA1.1.884789876.1712523082; __eoi=ID=1290dfaa789b83a7:T=1712523119:RT=1712533412:S=AA-Afjagvd6esLM1eZFtJaRdDJry; browsertoken=ca33d5e440a8a126d22e54366b2ceaecac94e76a",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.habbo-happy.net",
    "Referer": "https://www.habbo-happy.net/profile/javier2",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Te": "trailers"
}

num_requests = 1000  # Reemplaza esto con el número de veces que deseas enviar la solicitud

for i in range(num_requests):
    data = {
        "commentbody": f"BotSpammer by Aforak{i}",  # Añade el contador al comentario para hacerlo único
        "sendcomment": "Publicar"
        "replycomment"
    }
    response = requests.post(url, headers=headers, data=data)
    print("¡Publicado con éxito!")
