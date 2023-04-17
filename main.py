import requests


# Важно: Меняем только кукисы, остальные параметры оставляет неизменными
headers = {
      "authority": "www.itf-tennis-point.com",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                    " Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48",

      "Cookie": ""
}


session = requests.session() # Создаём новую сессию для без блокировочного хождения по сайту
session.headers = headers # Задаём параметры заголовков запрос с кукисами


