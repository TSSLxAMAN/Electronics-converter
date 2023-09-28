def binarychecker(binary):
    incorrectformat = ['2','3','4','5','6','7','8','9']
    for i in binary:
        if i in incorrectformat:
            return 0
    return 1


def octalchecker(octal):
    incorrectformat = ['9']
    for i in octal:
        if i in incorrectformat:
            return 0
    return 1


def binarytodecimal(binary):
    deciaml = 0
    for i in range(0,len(binary)):
        x = int(binary[i]) * (2**(len(binary)-i-1))
        deciaml = deciaml + x
    print(f"The decimal number is : {deciaml}")


def octaltodeciaml(octal):
    decimal = 0
    for i in range(0,len(octal)):
        x = int(octal[i])* (8**(len(octal)-i-1))
        decimal = decimal + x 
    print(f"The decimal number is : {decimal}")
    return 1


def deciamltobinary(decimal):
    list = []
    while decimal>=1:
        x = int(decimal % 2)
        decimal = decimal / 2
        list.append(x)
    list.reverse()
    binary = "".join(map(str,list))
    print(f"The binary is : {binary}")


def octaltobinary(octal):
    decimal = 0
    list = []
    for i in range(0,len(octal)):
        x = int(octal[i])*(8**(len(octal)-i - 1))
        decimal = decimal + x 
    while decimal>=1:
        y = int(decimal%2)
        decimal = decimal / 2
        list.append(y)
    list.reverse()
    binary = "".join(map(str,list))
    print(f"The bianry is : {binary}")
    

def deciamltooctal(decimal):
    list =  []
    while decimal>=1:
        x = int(decimal % 8)
        decimal = decimal / 8 
        list.append(x)
    list.reverse()
    octal = "".join(map(str,list))
    print(f"The octal is : {octal}")



def binarytooctal(binary):
    decimal = 0
    list = []
    for i in range(0,len(binary)):
        x = int(binary[i]) * (2 ** (len(binary) - i - 1))
        decimal = decimal + x
    while decimal>=1:
        y = int(decimal % 8)    
        decimal = decimal / 8
        list.append(y)
    list.reverse()
    octal = "".join(map(str,list))
    print(f"The octal is : {octal}")



while True:
    print("WELCOME ELECTRONIC CONVERTER\n1 = BINARY to DECIMAL\n2 = OCTAL to DECIMAL\n3 = DECIMAL to BINARY\n4 = OCTAL to BINARY\n5 = DECIMAL to OCTAL \n6 = BINARY to OCTAL\nChoose what do you want to do : ")
    userinput = int(input(""))
    match userinput:
        case 1:
            print("Enter the Bianry digit")
            binary = input("")
            result = binarychecker(binary)
            if result == 1:
                binarytodecimal(binary)
            else:
                print("Invalid Input")


        case 2:
            print("Enter the octal digit")
            octal = input("")
            result = octalchecker(octal)
            if result == 1:
                octaltodeciaml(octal)
            else:
                print("Invalid Input")


        case 3:
            print("Enter the decimal number : ")
            decimal = int(input())
            if decimal >=0:
                deciamltobinary(decimal)
            else:
                print("Invalid Input")
        
        
        case 4:
            print("Enter the octal number : ")
            octal = input("")
            result = octalchecker(octal)
            if result == 1:
                octaltobinary(octal)
            else: 
                print("Invalid input")

        
        case 5 :
            print("Enter the deciaml : ")
            decimal = int(input())
            if decimal<=0:
                print("Invalid Input")
            else:
                deciamltooctal(decimal)
        case 6:
            print("Enter the binary number : ")
            binary = input("")
            result = binarychecker(binary)
            if result == 1:
                binarytooctal(binary)
            else:
                print("Invalid input")
