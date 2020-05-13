from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generate(name):
    W,H=(512,220) #change width and height of center point of text accordingly
    R,G,B=(24,87,122) #change color of font
    fsize=42
    img = Image.open(t)     #  template
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype(f, size=fsize)   #  font selection
    w, h = draw.textsize(name,selectFont)
    draw.text(((W-(w/2)),(H-(h/2))), name , font=selectFont, fill=(R,G,B))  
    img.save("final_certificates/" + name + ".png","PNG")
    print("Generated " + name)


bad_chars = ['"'] 
t = input("Enter path or Drag and drop template: \n")
for i in bad_chars : 
    t= t.replace(i,"") 

f = input("Enter path or Drag and drop font: \n")
for i in bad_chars : 
    f= f.replace(i,"") 

o = input("Enter path or Drag and drop txt file: \n")
for i in bad_chars : 
    o= o.replace(i,"") 

fin = open(o,"r")

for i in fin:
    i=i.replace("\n","")
    generate(i)

fin.close()
