def makeBill() :
    total = 0
    name = input('Customer Name Please: ')
    NoOfItems = int(input('What Are The Total Number Of Items(number only): '))

    for item in range(1, NoOfItems + 1):
        cost = int(input(f"What is the cost of {item}st ? :  "))
        total = total + cost  


    print("__"*50)
    print("Name :", name)
    print('Total Cost :', total)
    print()
    print("*****Thank You For Shopping With Us*****")
    print('__'*50)

    total = 0


while True:
    newCustomer = input("Go To Next Person? (Y/y) / (N/n): ")

    if newCustomer == 'y' or newCustomer == 'Y':
        makeBill()

    elif newCustomer == 'n' or newCustomer == 'N':
        break

    else:
        print('Wrong Input')
