def menu():
    print("Welcome!\n1. Add contact\n2. Find contact\n3. Wiew contact list\n4. Change contact\n5. Exit ")

    a = input()
    return a

def get_contact():
    return [input('Input name: ')+" ", input('Input surname: ')+" ", input('Input phone number: ')]

def find_c():
    print("Choose parameter\n1. By name\n2. By surname\n3. By phone number ")
    b = input()
    return b 
