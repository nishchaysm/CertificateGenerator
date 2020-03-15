from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generate(name):
    img = Image.open("files/template.jpeg")     #  template
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype("files/Formata-Medium.otf", size=42)   #  font selection
    draw.text((455,200), name , font=selectFont, fill=(24, 87, 122))  
    img.save("final_certificates/" + name + ".png","PNG")
    print("Generated " + name)

fin = open(r'''files/new.txt''',"r")

for i in fin:
    i=i.replace("\n","")
    generate(i)

fin.close()
