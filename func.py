import interface, func

def add_contact(contact):
    # contact = [input('Input name: ')+" ", input('Input surname: ')+" ", input('Input phone number: ')]
    data = open('directory.txt', 'a')
    data.writelines(contact)
    data.write('\n')
    data.close()

# def find_contact():
#     contact_list = open('directory.txt', 'r')
#     search = input('Input surname: ')
#     for i in contact_list:
#         if search in i:
#             print(i)
#     contact_list.close()

def print_all():
    contact_list = open('directory.txt', 'r')
    num = 1
    for i in contact_list:
            print(f'{num}. {i}')
            num +=1
    contact_list.close()

def find_contact_n():
    contact_list = open('directory.txt', 'r')
    search = input('Input name: ')
    for i in contact_list:
        if search in i:
            print(i)
    contact_list.close()

def find_contact_s():
    contact_list = open('directory.txt', 'r')
    search = input('Input surname: ')
    for i in contact_list:
        if search in i:
            print(i)
    contact_list.close()

def find_contact_num():
    contact_list = open('directory.txt', 'r')
    search = input('Input surname: ')
    for i in contact_list:
        if search in i:
            print(i)
    contact_list.close()  

def find_contact():
    contact_list = open('directory.txt', 'r')
    flag = True
    while flag:
        if a == '1':
            func.find_contact_n(interface.get_contact())
            
        elif a == '2':
            func.find_contact_s()
            
        elif a == '3':
            func.find_contact_num()
            
        else:
            flag = False

    contact_list.close()