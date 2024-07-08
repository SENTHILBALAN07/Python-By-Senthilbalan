number=input("Phone:")
dic={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
x=""
for i in number:
    x+=dic.get(i,"!")+" "
print(x)


