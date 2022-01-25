def swap():
    input1=input("enter file name 1:")
    input2=input("enter file name 2:")
    u = open(input2,"r")
    v = open(input1,"r")

    data_u = u.read()
    data_v = v.read()

    u = open(input2,"w")
    u.write(data_v)

    v = open(input1,"w")
    v.write(data_u)
    
swap()