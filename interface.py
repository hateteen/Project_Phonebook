def menu():
    print("Welcome!\n1. Add contact\n2. Find contact\n3. Wiew contact list\n4. Exit")

    a = input()
    return a

def get_contact():
    return [input('Input name: ')+" ", input('Input surname: ')+" ", input('Input phone number: ')]

def find_c():
    return [input('By name: ')+" ", input('By surname: ')+" ", input('By phone number: ')]
