import interface
def add_contact(contact):
    data = open('directory.txt', 'a')
    data.writelines(contact)
    data.write('\n')
    data.close()

def print_all():
    contact_list = open('directory.txt', 'r')
    num = 1
    for i in contact_list:
            print(f'{num}. {i}')
            num +=1
    contact_list.close()

def find_contact():
    contact_list = open('directory.txt', 'r')
    b = interface.find_c()
    flag2 = True
    while flag2:
        if b == '1':
            search = input('Input name: ')
            for i in contact_list:
                if search in i:
                    print(i)
            flag2 = False
        elif b == '2':
            search = input('Input surname: ')
            for i in contact_list:
                if search in i:
                    print(i)
            flag2 = False  
        elif b == '3':
            search = input('Input phone number: ')
            for i in contact_list:
                if search in i:
                    print(i)
            flag2 = False

def change_contact():
    contact_list = open('directory.txt','r')
    change_list = []
    changed_name = input ('Input surname to change: ')
    fill_to_change = input('Input parameter ("Name", "Surname" or "Phone number"): ')
    new_value = input(f"Input new data {fill_to_change} ")

    for i in contact_list:
        if changed_name in i:
            fields = i.split()
            if fill_to_change == 'Name':
                fields[0] = new_value
            elif fill_to_change == 'Surname':
                fields[1] = new_value
            elif fill_to_change == 'Phone number':
                fields[2] = new_value
            changed_line = ' '.join(fields) + '\n'
            change_list.append(changed_line)
        else:
            change_list.append(i)
    contact_list.close()
    

    contact_list = open('directory.txt','w')
    for i in change_list:
        contact_list.writelines(i)
    contact_list.close()

