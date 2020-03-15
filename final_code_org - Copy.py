from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generate(name):
    img = Image.open(t)     #  template
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype(f, size=42)   #  font selection
    draw.text((430,360), name , font=selectFont, fill=(24, 87, 122))  
    img.save("final_certificates/" + name + ".png","PNG")
    print("Generated " + name)


t = input("Enter path or Drag and drop template: \n")
f = input("Enter path or Drag and drop font: \n")
o = input("Enter path or Drag and drop txt file: \n")
fin = open(o,"r")

for i in fin:
    i=i.replace("\n","")
    generate(i)

fin.close()
