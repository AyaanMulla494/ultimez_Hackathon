ind = int(input("Enter Number of Individuals:"))
slices = [8,6,4,1]
# large = int(ind/8)
# ind%=8
# medium = int(ind/6)
# ind%=6
# reg = int(ind/4)
# ind%=4
# small = ind
# print(f"We will have {large} Large pizza\n")
# print(f"We will have {medium} Medium pizza\n")
# print(f"We will have {reg} Regular pizza\n")
# print(f"We will have {small} Small pizza\n")
pizza=[]
for item in slices:
    pizza.append(int(ind/item))
    ind = ind%item

print(f"We will have {pizza[0]} Large pizza\n")
print(f"We will have {pizza[1]} Medium pizza\n")
print(f"We will have {pizza[2]} Regular pizza\n")
print(f"We will have {pizza[3]} Small pizza\n")
