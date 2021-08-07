

interior_walls = int(input())
exterior_walls = int(input())
if interior_walls:
    int_walls = []
    for i in range(interior_walls):
        int_walls.append(float(input()))

if exterior_walls:
    ext_walls = []
    for i in range(exterior_walls):
        ext_walls.append(float(input()))
if exterior_walls < 0 or interior_walls < 0:
    print("Invalid Input")
    exit()
if exterior_walls and interior_walls:
    print("Total estimated Cost : ",(sum(int_walls)*18+sum(ext_walls)*12),"INR")
else:
    if exterior_walls:
        print("Total estimated Cost : ",sum(ext_walls)*12,"INR")
    elif interior_walls:
         print("Total estimated Cost : ",sum(int_walls)*18,"INR")
    else:
        print("Total estimated Cost : 0.0 INR")