from PIL import Image, ImageFont, ImageDraw
from datetime import date


image = Image.open("post.png")
draw = ImageDraw.Draw(image)

#for adding the heading text to the image.
font = ImageFont.truetype("Inter-Medium.ttf", size=50)
content = "Latest Weather Forecast!"
color = "rgb(255, 255, 255)" 
(x, y) = (45, 55)
draw.text((x, y), content, color, font=font)


#for adding the date of the forecast
font = ImageFont.truetype("Inter-Medium.ttf", size=30)
today = date.today()
content = date.today().strftime("%A - %B %m %Y")
color = "rgb(255, 255, 255)" 
(x, y) = (45, 145)
draw.text((x, y), content, color, font=font)

image.show()
image.save("test.png")
print("it is working")