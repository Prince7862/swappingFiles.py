def swapFileData():
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")
    a = file1
    b = file2

    with open(file1, 'r') as a:
        data_a = a.read()
        print(data_a)
    
    with open(file2, 'r') as b:
        data_b = b.read()
        print(data_b)

    with open(file1, 'w') as a:
        a.write(data_b)
        print(data_b)

    with open(file2, 'w') as b:
        b.write(data_a)
        print(data_a)
   
swapFileData()
