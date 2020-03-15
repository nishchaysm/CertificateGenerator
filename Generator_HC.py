from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generate(name):
    W,H=(512,220) #change width and height of center point of text accordingly
    r,g,b=(24,87,122) #change color of font
    img = Image.open("files/template.jpeg")     #  template
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype("files/Formata-Medium.otf", size=42)   #  font selection
    w,h = draw.textsize(name,selectFont)
    draw.text(((W-(w/2)),(H-(h/2))), name , font=selectFont, fill=(r,g,b))
    img.save("final_certificates/" + name + ".png","PNG")
    print("Generated " + name)

fin = open(r'''files/name.txt''',"r")

for i in fin:
    generate(i.strip())

fin.close()
