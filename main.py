from PIL import Image, ImageFont, ImageDraw

#for adding the heading text to the image.

image = Image.open("post.png")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("Inter-Medium.ttf", size=50)
content = "Latest Weather Forecast!"
color = "rgb(255, 255, 255)" 
(x, y) = (45, 55)
draw.text((x, y), content, color, font=font)


image.save("test.png")

print("it is working")