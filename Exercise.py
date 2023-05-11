import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

api_key = "481a07a08188143ec9b4f106c0f630ec"  # Update Your API Here
position = [600, 800, 985, 1170, 1350]

uk_list = ["London", "Manchester", "Edinburgh", "Bristol", "Birmingham"]
india_list = ["Jaipur", "Delhi", "Mumbai", "Kolkata", "Chennai"]
af_list = ["Nigeria", "Ghana", "Gambia", "morocco", "Algeria"]
country_list = [uk_list, india_list, af_list]

for country in country_list:
    image = Image.open("story.png")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Inter.ttf', size=60)
    content = "Instagram weather forecast"
    color = 'rgb(255, 255, 255)'
    (x, y) = (150, 200)
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype('Inter.ttf', size=45)
    content = date.today().strftime("%A - %B %d, %Y")
    color = 'rgb(255, 255, 255)'
    (x, y) = (150, 325)
    draw.text((x, y), content, color, font=font)

    index = 0
    for city in country:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        font = ImageFont.truetype('Inter.ttf', size=60)
        color = 'rgb(0, 0, 0)'
        (x, y) = (120, position[index])
        draw.text((x, y), city, color, font=font)

        try:
            font = ImageFont.truetype('Inter.ttf', size=60)
            content = str(data['main']['temp']) + "\u00b0"
            color = 'rgb(255, 255, 255)'
            (x, y) = (600, position[index])
            draw.text((x, y), content, color, font=font)

            content = str(data['main']['humidity']) + "%"
            color = 'rgb(255, 255, 255)'
            (x, y) = (850, position[index])
            draw.text((x, y), content, color, font=font)

        except KeyError:
            print(f"Error: Weather data not found for {city}")

        index += 1

    image.save(str(date.today()) + country[0] + ".png")
    image_pdf = image.convert('RGB')
