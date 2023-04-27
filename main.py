import interface, func

def main_prog():
    flag = True
    while flag:
        a = interface.menu()

        if a == '1':
            func.add_contact(interface.get_contact())

        elif a == '2':
            func.find_contact(interface.find_c())
            

        elif a == '3':
            func.print_all()

        else:
            flag = False
main_prog()