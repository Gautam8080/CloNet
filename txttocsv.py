import csv
from PIL import Image

list_cloth=open("list_category_cloth.txt","r")
list_bbox=open("list_bbox.txt","r")
list_cloth.readline()
list_cloth.readline()
list_bbox.readline()
list_bbox.readline()
lines_cloth=list_cloth.readlines()
lines_bbox=list_bbox.readlines()
all_clothes=["Anorak","Blazer","Blouse","Bomber","Button-Down","Cardigan","Flannel","Halter","Henley","Hoodie","Jacket","Jersey","Parka","Peacoat","Poncho","Sweater","Tank","Tee","Top","Turtleneck","Capris","Chinos","Culottes","Cutoffs","Gauchos","Jeans","Jeggings","Jodhpurs","Joggers","Leggings","Sarong","Shorts","Skirt","Sweatpants","Sweatshorts","Trunks","Caftan","Cape","Coat","Coverup","Dress","Jumpsuit","Kaftan","Kimono","Nightdress","Onesie","Robe","Romper","Shirtdress","Sundress"]
ncsv=open("newcsv.csv","w")
# print(lines_bbox[0])
# temp_bbox=lines_bbox[0].split()
# im = Image.open(temp_bbox[0])
# width,height=im.size
# print(temp_bbox)
# print(width,height)
ncsv.write("filename,width,height,class,xmin,ymin,xmax,ymax")
ncsv.write("\n")
counter=0
for line in lines_bbox:
    temp=line.split()
    index=-1
    type_of_cloth=""
    for cloth in all_clothes:
        index=temp[0].find(cloth)
        if(index!=-1):
            type_of_cloth=cloth
            break
    if(index==-1):
        continue
    ncsv.write(temp[0])
    ncsv.write(",")
    im=Image.open(temp[0])
    width,height=im.size
    ncsv.write(str(width))
    ncsv.write(",")
    ncsv.write(str(height))
    ncsv.write(",")
    ncsv.write(type_of_cloth)
    ncsv.write(",")
    ncsv.write(temp[1])
    ncsv.write(",")
    ncsv.write(temp[2])
    ncsv.write(",")
    ncsv.write(temp[3])
    ncsv.write(",")
    ncsv.write(temp[4])
    ncsv.write("\n")
    print("writing on line")
ncsv.close()
print("Completed")
