from datetime import datetime
now = datetime.now()
file_list = ['testowy1.txt', 'testowy2.txt']

file_dict = {
    't1':'C:\\Users\\Dell\\Desktop\\test_txt_files\\testowy1.txt',
    't2':'C:\\Users\\Dell\\Desktop\\test_txt_files\\testowy2.txt',
}

def writing(arg_txt):  # editing document function
    while True:
        option = input('choose option: add - add new record, read - read records, exit - exit ')
        if option == 'add':
            file_1 = open(arg_txt, 'a')
            file_1.write(f'{str(now.strftime("%d-%m-%Y, %H:%M:%S"))}: {input("kolejny rekord: ")}\n')
            file_1.close()
        elif option == 'read':
            file_1 = open(arg_txt, 'r')
            print(file_1.read())
        elif option == 'exit':
            break
        else:
            print('Wrong communicate. Type again.')


while True:  # this way uses DICTIONARY
    print('what do you want to do?')
    my_choice = input('file doc - doc, exit - exit: ')
    print('choose modificated folder or exit')
    if my_choice == 'doc':
        writing(file_dict[input('t1 or t2 :')])  # writing is my function
    elif my_choice == 'exit':
        break
    else:
        print('Wrong communicate. Type again.')


# while True:  # this way uses LIST
#     my_file = input('choose document: test1 or test2: ')
#     if my_file == 'test1':
#         writing(file_list[0])
#     elif my_file == 'test2':
#         writing(file_list[1])
#     elif my_file == exit:
#         break
#     else:
#         print('Wrong communicate. Type again.')
