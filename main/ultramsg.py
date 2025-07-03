import requests




payload = payload.encode('utf8').decode('iso-8859-1')
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)


def message(phone, name):
    url = "https://api.ultramsg.com/instance117654/messages/chat"
    body = (
        f"Здравствуйте, {name}!\n"
        "С вами ФРАНШИЗА YAPOSHKIN ROLLS.\n"
        "Откройте прибыльный бизнес с франшизой доставки суши Yaposhkin Rolls. "
        "Мы предлагаем готовую бизнес-модель с минимальными вложениями, быстрым запуском "
        "и высокой рентабельностью. Франчайзи получают раскрученный бренд, продуманное меню, "
        "автоматизированную IT-систему, маркетинговую поддержку и полный набор инструментов "
        "для успешного старта."
    )
    payload = {
        "token": "1jvy6osrh43bbncn",
        "to": phone,
        "body": body
    }
    response = requests.post(url, data=payload)
    return response
