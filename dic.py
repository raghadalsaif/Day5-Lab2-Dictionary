



dict1 = {

    1: {"Name": "Amal",  "Number": 1111111111},
    2: {"Name": "Mohammed", "Number": 2222222222},
    3: {"Name": "Khadijah", "Number": 3333333333},
    4: {"Name": "Abdullah", "Number": 4444444444},
    5: {"Name": "Rawan", "Number": 5555555555},
    6: {"Name": "Faisal", "Number": 6666666666},
    7: {"Name": "Layla", "Number": 7777777777}
}
print(dict1)

for k in dict1:
    print("phone id is:", k)
# this will print for me the key just but if i wint to print the value also
theNum = int(input("please enter the number you look for"))


def numlen(thenum):
    if thenum < 10 or thenum > 10:
        print("This is invalid number")

numlen(theNum)
"""
for k, v in dict1.items():
    if theNum == v['Number']:
        print("the name of the phone is :", v['Name'])
    else:
        print("Sorry, the number is not found")"""
for k, v in dict1.items():
    if theNum == v['Number']:
        print(v)




while True:
    for key, value in dict1.items():
        if int(theNum) == value["Number"]:
            print("the name of the phone is :", value['Name'])
            break
        else:
            print("Sorry, the number is not found")
"""for i in dict1.items():
    if theNum == dict1.values():
        x = dict1.get(i)
        print(x)
    else:
        print("Sorry, the number is not found")

for i in dict1.items():
    if theNum == dict1["Number"]:
        x = dict1.get(i)
        print(x)
    else:
        print("Sorry, the number is not found")


def owner(ownerNum):
    if ownerNum == 1:
        print(dict1.values())
    else:
        print("Sorry, the number is not found")


"""
