import re

s = open("tokens.txt", "w", encoding="utf-8")

f = open("ann_1500.txt", "r", encoding="utf-8")
text = f.read()
tokens = text.split()

res_station = re.findall("[•]*[А-Я][а-яё]+ [мМ][\.]*", text)
res_appart = re.findall("1-комн[\.]* кв-ру,", text)
res_minutes = re.findall("[0-9]+? м[\.]*[ин]*[/]*[.]*п*[,]*[.]*[еш]*[к]*[ом]*[,]*", text)
res_street = re.findall("[А-Я][а-яё]+ [ул\.,]*[пер\.,]*[вал,]*", text)
res_house = re.findall("д[\.]* [0-9]+[/]*[0-9]+[;]*", text)
res_building = re.findall("корп[\.]* [0-9]+?[,]", text)
res_square = re.findall("[0-9]+[.,0-9]*[/][0-9]+[.,0-9]*[/]*[0-9]+[.,0-9]* кв.м,", text)
res_square_kitchen = re.findall("кух[ня]* [0-9]+?[\.]*[0-9]*[,]", text)
res_square_loggia = re.findall("лоджия [0-9]+?[\.]*[0-9]*", text)
res_floor = re.findall("[0-9]+[/-][0-9]+ эт[\.]*[,]*", text)
res_price = re.findall("[0-9]+ тыс.дол[\.]*", text)
res_phone = re.findall("Т[\.]* [0-9-]+[,]*", text)

i = 0
count = 0

while i < len(tokens):
    tokens[i] = tokens[i].strip(".")
    tokens[i] = tokens[i].strip(",")
    tokens[i] = tokens[i].strip(";")
    tokens[i] = tokens[i].strip(".,")

    if tokens[i] == "в":
        tokens[i] == "в"
        count += 1
        s.write(str(count) + "   " + tokens[i] + "\n")
        i += 1
        
    for element in res_station:
        if tokens[i] in element and tokens[i+1] in element:
            tokens[i] = tokens[i] + " " + tokens[i+1]
            count += 1
            s.write(str(count) + "   " + tokens[i].strip(".") + "\n")
            i += 2
              
    for element in res_appart:
         if tokens[i] in element and tokens[i+1] in element:
             tokens[i] = tokens[i] + " " + tokens[i+1]
             count += 1
             s.write(str(count) + "   " + tokens[i].strip(",") + "\n")
             i += 2
              
    for element in res_minutes:
         if tokens[i] in element and tokens[i+1] in element:
              tokens[i] = tokens[i] + " " + tokens[i+1]
              count += 1
              s.write(str(count) + "   " + tokens[i].strip(",") + "\n")
              i += 2
              
    for element in res_street:
         if tokens[i] in element and tokens[i+1] in element:
              tokens[i] = tokens[i] + " " + tokens[i+1]
              count += 1
              s.write(str(count) + "   " + tokens[i].strip(".,") + "\n")
              i += 2

    for element in res_house:
         if tokens[i] in element and tokens[i+1] in element:
              tokens[i] = tokens[i] + " " + tokens[i+1]
              count += 1
              s.write(str(count) + "   " + tokens[i].strip(";") + "\n")
              i += 2

    for element in res_building:
         if tokens[i] in element and tokens[i+1] in element:
              tokens[i] = tokens[i] + " " + tokens[i+1]
              count += 1
              s.write(str(count) + "   " + tokens[i].strip(",") + "\n")
              i += 2
              
    for element in res_square:
         if tokens[i] in element and tokens[i+1] in element:
              tokens[i] = tokens[i] + " " + tokens[i+1]
              count += 1
              s.write(str(count) + "   " + tokens[i].strip(",") + "\n")
              i += 2

    for element in res_square_kitchen:
         if tokens[i] in element and tokens[i+1] in element:
              tokens[i] = tokens[i] + " " + tokens[i+1]
              count += 1
              s.write(str(count) + "   " + tokens[i].strip(",") + "\n")
              i += 2

    for element in res_square_loggia:
        if tokens[i] in element and tokens[i+1] in element:
            tokens[i] = tokens[i] + " " + tokens[i+1]
            count += 1
            s.write(str(count) + "   " + tokens[i] + "\n")
            i += 2
              
    for element in res_floor:
         if tokens[i] in element and tokens[i+1] in element:
              tokens[i] = tokens[i] + " " + tokens[i+1]
              count += 1
              s.write(str(count) + "   " + tokens[i].strip(",") + "\n")
              i += 2
              
    for element in res_price:
        if tokens[i] in element and tokens[i+1] in element:
            tokens[i] = tokens[i] + " " + tokens[i+1]
            count += 1
            s.write(str(count) + "   " + tokens[i].strip(".") + "\n")
            i += 2
             
    for element in res_phone:
         if tokens[i] in element:
              tokens[i] = tokens[i] + " " + tokens[i+1]
              count += 1
              s.write(str(count) + "   " + tokens[i].strip(",") + "\n")
              i += 2
    
    count += 1
    tokens[i] = tokens[i].strip(".")
    tokens[i] = tokens[i].strip(",")
    tokens[i] = tokens[i].strip(";")
    tokens[i] = tokens[i].strip(".,")
    s.write(str(count) + "   " + tokens[i] + "\n")
    i += 1

s.close()

