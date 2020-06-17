import requests

def baixar_arquivo(url, endereco):
    resposta = requests.get(url, headers=headers)

    with open(endereco, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
    print("Downloaded, save in {}".format(endereco))

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
  }

continuar = "Y"
while continuar == "Y":
    url = input("Digite a url da imagem: ")
    req = requests.get(url, headers=headers)
    html = str(req.content)

    inicio = html.find('"shortcode":')
    inicio += 13
    fim = html.find(',"dimens')
    fim -= 1
    imgName = ""
    for i in range(inicio, fim):
        imgName += html[i]

    inicio = html.find('"display_url":')
    inicio += 15
    fim = html.find(',"display_resources')
    fim-=1
    imgURL = ""
    for i in range(inicio, fim):
        imgURL += html[i]
    imgURL = imgURL.replace("\\\\u0026", "&")

    baixar_arquivo(imgURL, "C:\\Users\\produ\\Pictures\\meninos\\{}.jpg".format(imgName))
    continuar = input("\n Quer continuar? [Y/N]:")