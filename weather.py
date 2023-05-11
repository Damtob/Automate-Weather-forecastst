import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

api_key = "481a07a08188143ec9b4f106c0f630ec"  # Update Your API Here
position = [300, 430, 555, 690, 825]

uk_list = ["London", "Manchester", "Edinburgh", "Bristol", "Birmingham"]
india_list = ["Jaipur", "Delhi", "Mumbai", "Kolkata", "Chennai"]
af_list = ["Nigeria", "Ghana", "Gambia", "morocco", "Algeria"]
country_list = [uk_list, india_list, af_list]

for country in country_list:
    image = Image.open("post.png")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Inter.ttf', size=50)
    content = "Latest Weather Forecast"
    color = 'rgb(255, 255, 255)'
    (x, y) = (55, 50)
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype('Inter.ttf', size=30)
    content = date.today().strftime("%A - %B %d, %Y")
    color = 'rgb(255, 255, 255)'
    (x, y) = (55, 145)
    draw.text((x, y), content, color, font=font)

    index = 0
    for city in country:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        font = ImageFont.truetype('Inter.ttf', size=50)
        color = 'rgb(0, 0, 0)'
        (x, y) = (135, position[index])
        draw.text((x, y), city, color, font=font)

        try:
            font = ImageFont.truetype('Inter.ttf', size=50)
            content = str(data['main']['temp']) + "\u00b0"
            color = 'rgb(255, 255, 255)'
            (x, y) = (600, position[index])
            draw.text((x, y), content, color, font=font)

            content = str(data['main']['humidity']) + "%"
            color = 'rgb(255, 255, 255)'
            (x, y) = (810, position[index])
            draw.text((x, y), content, color, font=font)

        except KeyError:
            print(f"Error: Weather data not found for {city}")

        index += 1

    image.save(str(date.today()) + country[0] + ".png")
    image_pdf = image.convert('RGB')
