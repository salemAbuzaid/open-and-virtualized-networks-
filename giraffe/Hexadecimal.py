
def hex_to_dec(hex):
    num = {"0":0 ,"1":1 , "2": 2, "3":3, "4": 4, "5" : 5 ,"6":6 ,"7": 7 ,"8":8 ,
        "9":9 , "a":10 , "b":11 , "c":12 , "d": 13, "e": 14 , "f":15}
    x= 1
    res= 0
    for i in hex:
        res= res + num.get(i.lower()) * (16 ** (len(hex)-x))
        x+=1
    print("the conversion from hexadecimal to decimal: ",res)
    #to_binary(res)
def dec_to_hex(dec):
    num={
        "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8",
        "9": "9", "10":"A" ,"11":"B", "12":"C", "13":"D", "14":"E", "15":"F"
    }

    list =[]
    base =16
    while int(dec / base) > 0 or (dec % base) != 0:
        list.append(num.get(str(dec % base)))
        dec = int(dec / base)
    list.reverse()
    print("the hexadecimal number is=", list)

dec =""
if __name__ == "__main__":
    hex =""
    while hex != "end":
        hex = input("enter a hexadecimal number or write end: ")
        if hex != "end":
            flag = 0
            for digit in hex:
                if digit.lower() not in "0123456789abcdef":
                    flag =1
            if flag == 0:
                hex_to_dec(hex)

    while dec != "end":
        dec = input("enter a decimal number or write end: ")
        if dec.isnumeric():
            if dec != "end":
                dec_to_hex(int(dec))
