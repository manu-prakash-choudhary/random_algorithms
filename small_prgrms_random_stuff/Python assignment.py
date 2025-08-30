# Raman Mallya 20BAI10322

# binary to decimal
def binaryToDecimal(n):
	num = n;
	dec_value = 0;
	base = 1;
	
	temp = num;
	while(temp):
		last_digit = temp % 10;
		temp = int(temp / 10);
		
		dec_value += last_digit * base;
		base = base * 2;
	print(dec_value)

# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
	
	if num >= 1:
		DecimalToBinary(num // 2)
	print(num % 2, end = '')

def binaryToOctal(binarynum):
    octaldigit = 0
    octalnum = []
    i = 0
    mul = 1
    chk = 1
    while binarynum!=0:
        rem = binarynum % 10
        octaldigit = octaldigit + (rem * mul)
        if chk%3==0:
            octalnum.insert(i, octaldigit)
            mul = 1
            octaldigit = 0
            chk = 1
            i = i+1
        else:
            mul = mul*2
            chk = chk+1
        binarynum = int(binarynum / 10)

    if chk!=1:
        octalnum.insert(i, octaldigit)

    print("\nEquivalent Octal Value = ", end="")
    while i>=0:
        print(str(octalnum[i]), end="")
        i = i-1

def octalToBinary(octnum):

    rev = 0
    chk = 0

    while octnum!=0:
        rem = octnum%10
        if rem>7:
            chk = 1
            break
        rev = rem + (rev*10)
        octnum = int(octnum/10)

    if chk == 0:
        octnum = rev
        binnum = ""

        while octnum!=0:
            rem = octnum%10
            if rem==0:
                binnum = binnum + "000"
            elif rem==1:
                binnum = binnum + "001"
            elif rem==2:
                binnum = binnum + "010"
            elif rem==3:
                binnum = binnum + "011"
            elif rem==4:
                binnum = binnum + "100"
            elif rem==5:
                binnum = binnum + "101"
            elif rem==6:
                binnum = binnum + "110"
            elif rem==7:
                binnum = binnum + "111"
            octnum = int(octnum/10)

        print("\nEquivalent Binary Value = ", binnum)

    else:
        print("\nInvalid Input!")



# decimal value to hexadecimal value
def decimalToHexadecimal(decimal):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',5: '5', 6: '6', 7: '7',8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexadecimal = '';
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    print( hexadecimal)

# hexadecimal to decimal
def hexToDec(hexadecimal):
    hex_to_dec_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    hex = hexadecimal.strip().upper()
    dec = 0
    length = len(hex) -1
    for digit in hex:
        dec += hex_to_dec_table[digit]*16**length
        length -= 1
    
    print("Decimal value is : ",dec)



#hexadecimal to Binary
def hexToBinary(ini_string):
    print ("Initial string", ini_string)

    # Code to convert hex to binary
    n = int(ini_string, 16)
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1	
    res = bStr

    # Print the resultant string
    print ("Resultant string", str(res))



# binary number into hexadecimal number
def binToHexa(n):
	bnum = int(n)
	temp = 0
	mul = 1
	count = 1
	hexaDeciNum = ['0'] * 100
	i = 0
	while bnum != 0:
		rem = bnum % 10
		temp = temp + (rem*mul)
		if count % 4 == 0:
			
			# check if temp < 10
			if temp < 10:
				hexaDeciNum[i] = chr(temp+48)
			else:
				hexaDeciNum[i] = chr(temp+55)
			mul = 1
			temp = 0
			count = 1
			i = i+1
		else:
			mul = mul*2
			count = count+1
		bnum = int(bnum/10)
		
	if count != 1:
		hexaDeciNum[i] = chr(temp+48)
		
	if count == 1:
		i = i-1
		
	print("\n Hexadecimal equivalent of {}: ".format(n), end="")
	while i >= 0:
		print(end=hexaDeciNum[i])
		i = i-1

def rightShift(num):
    print("num >> 1 =", num >> 1)

def leftShift(num):
    print("num << 1 =", num << 1)


print("Choose one of the following : ")
print("  1. Binary to Decimal\n ",

"2. Decimal to Binary\n ",

"3. Binary to Octal\n ",

"4. Octal to Binary\n ",

"5. Decimal to Hexadecimal\n ",

"6. Hexadecimal to Decimal\n ",

"7. Hexadecimal to Binary\n ",

"8. Binary to Hexadecimal\n ",

"9. Left Shifting\n ",

"10. Right Shifting\n ")

option = int(input("Enter Your Choice : "))
if option ==1:
    bin = int(input())
    binaryToDecimal(bin)
elif option==2:
    dec = int(input())
    DecimalToBinary(dec)

elif option==3:
    bin = int(input())
    binaryToOctal(bin)
elif option==4:
    oct = int(input())
    octalToBinary(oct)
elif option==5:
    dec = int(input())
    decimalToHexadecimal(dec)
elif option==6:
    hex = input()
    hexToDec(dec)
elif option==7:
    hex =input()
    hexToBinary()
elif option==8:
    hex = input()
    binToHexa(hex)
elif option==9:
    num = int(input())
    leftShift(num)
else:
    num =int(input())
    rightShift(num)
