for i in range (0, 151):
    print (i)
print ("________________________")

for i in range (5,1001):
    if (i%5 == 0):
        print(i)

print ("________________________")
for i in range (1,101):
    if i % 10 == 0:
        print ("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
print ("________________________")

sumaImpares= 0 
for i in range (0, 500001):
    if i % 2 == 1:
        print (i)
        sumaImpares += i
print (sumaImpares)
print ("________________________")

for i in range (2018, 0, -4):
        print (i)
print ("________________________")

lowNum=2
highNum=9
mult=3
for i in range (lowNum, highNum+1):
    if (i % mult == 0): 
        print (i)
    
        