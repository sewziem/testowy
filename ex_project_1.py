from datetime import datetime
now = datetime.now()
file_list = ['testowy1.txt', 'testowy2.txt']

file_dict = {
    't1':'C:\\Users\\Dell\\Desktop\\test_txt_files\\testowy1.txt',
    't2':'C:\\Users\\Dell\\Desktop\\test_txt_files\\testowy2.txt',
}
file_keys = file_dict.keys()

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
        while True:
            take_a_key = input(f'choose doc {file_keys}: ')
            if take_a_key in file_keys:
                writing(file_dict[take_a_key])  # writing is my function
            elif take_a_key == 'exit':
                break
            else:
                print('type again ')
        
    elif my_choice == 'exit':
        break
    else:
        print('Wrong communicate. Type again.')



