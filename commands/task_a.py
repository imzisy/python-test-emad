import string
import random
import os


def random_real_number():
    length = random.randint(1, 10)
    output = round(random.uniform(10, 20), length)
    return '{}'.format(output)


def random_integer():
    return '{}'.format(random.randint(10, 20))


def random_alphanumerics():
    size = random.randint(10, 20)
    random_string = ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=size))
    return add_spaces(random_string)


def random_string():
    size = random.randint(10, 20)
    return ''.join(random.choices(string.ascii_uppercase, k=size))


def add_spaces(str):
    number_of_spaces_before = random.randint(0, 9)
    number_of_spaces_after = random.randint(0, 9)
    return ' ' * number_of_spaces_before + str + ' ' * number_of_spaces_after


def main():
    fileName = './file.txt'
    open(fileName, 'w')
    fileSize = os.stat(fileName).st_size

    with open(fileName, 'a') as myFile:
        print('started ...')
        while fileSize < 10485760:
            
            function_list = [
                random_alphanumerics, random_string, random_integer,
                random_real_number
            ]
            dataType = random.choice(function_list)
            output = dataType()
            myFile.write(output + ', ')
            fileSize = os.stat(fileName).st_size

        print('End')
        myFile.close()

main()