dict1 = {

    1: {"Name": "Amal",  "Number": 1111111111},
    2: {"Name": "Mohammed", "Number": 2222222222},
    3: {"Name": "Khadijah", "Number": 3333333333},
    4: {"Name": "Abdullah", "Number": 4444444444},
    5: {"Name": "Rawan", "Number": 5555555555},
    6: {"Name": "Faisal", "Number": 6666666666},
    7: {"Name": "Layla", "Number": 7777777777}
}


while True:
    thenum = input("pleas inter the num")
    if len(thenum) != 10:
        print("This is invalid number (Phone numbers should contain 10 digit)")
        continue
    elif thenum.isdigit() == False:
        print("This is invalid number (contains letters or symbols)")
    else:
        x = True
        for k, v in dict1.items():
            if int(thenum) == v["Number"]:
                x = False
                print("Owner is ", v["Name"])
                break