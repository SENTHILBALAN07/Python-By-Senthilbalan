value=int(input('Enter the value : '))
unit=input("K or p: " )
b=unit.upper()
if b=="K":
    pounds = float(value * 0.45)
    print('The accurate value is in', pounds, 'pounds')
elif b=="P":
    kilogram=float(value/0.45)
    print('The accurate value is in', kilogram, 'kilo')
else:
    print("The correct statement")



