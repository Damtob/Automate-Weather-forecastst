import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

api_key = "b39dbc2c95d91b47ac546f193b3102be"
position = [605, 795, 875, 1175, 1365]

Nigeria_list = ["Lagos", "Ibadan", "Abuja", "Kano", "Jos"]
South_Africa_list = ["Pretoria", "Johannesburg", "Cape Town", "East London", "Soweto"]
Ghana_list =["Accra", "Kumasi", "Tema", "Cape Coast", "Obuasi"]
country_list = [Nigeria_list, South_Africa_list, Ghana_list]

for country in country_list:
    image = Image.open("post.png")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Inter.ttf', size=50)
    content = "Latest Weather Forecast"
    color = 'rgb(255, 255, 255)'
    (x, y) = (85, 165)
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype('Inter.ttf', size=30)
    content = date.today().strftime("%A - %B, %d, %Y")
    color = 'rgb(255, 255, 255)'
    (x, y) = (85, 325)
    draw.text((x, y), content, color, font=font)

    index = 0
    for city in country:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=b39dbc2c95d91b47ac546f193b3102be&units=metric".format(
            city)
        response = requests.get(url)
        data = json.loads(response.text)

        font = ImageFont.truetype('Inter.ttf', size=50)
        color = 'rgb(0, 0, 0)'
        (x, y) = (75, position[index])
        draw.text((x, y), city, color, font=font)

        font = ImageFont.truetype('Inter.ttf', size=50)
        content = str(data['main']['temp']) + "\u00b0"
        color = 'rgb(255, 255, 255)'
        (x, y) = (605, position[index])
        draw.text((x, y), content, color, font=font)

        font = ImageFont.truetype('Inter.ttf', size=50)
        content = str(data['main']['humidity']) + "%"
        color = 'rgb(255, 255, 255)'
        (x, y) = (845, position[index])
        draw.text((x, y), content, color, font=font)

        index += 1

    image.save(str(date.today()) + country[0] + ".png")


