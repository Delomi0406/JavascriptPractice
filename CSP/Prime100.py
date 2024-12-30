no=[]
yes=[]

for index in range (2,101):
    for i in range (2, int((index**0.5)+1)):
        if index % i ==0:
            no.append(index)
            break
    else:
        yes.append(index)
print("no", no)
print("yes", yes)