i=1

print("XXX", end =" ")
print("   ", end =" ")

while i <= 10:
    
    print("%03d" % (i,),end = " ")
    i= i+1
i = 1
j = 1
print("")
print("")

while i <= 10:

    print("%03d" % (i,),end = " ")
    print("   ", end =" ")


    while j <= 10:
        k = i*j
        print("%03d" % (k,), end = " ")
        j = j + 1

    j = 1
    print("")
    i = i + 1