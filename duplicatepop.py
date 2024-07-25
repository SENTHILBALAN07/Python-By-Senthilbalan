a=[34,43,43,56,64,54,56]
new=[]
for i in a:
    if i not in new:
        new.append(i)
print(new)
