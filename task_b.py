def get_object_type(item):
    if item.isdigit():
        return item + ' - integer'

    if item.rfind('.') > 0:
        return item + ' - real numbers'

    if item.isalpha():
        return item + ' - strings'

    if item.isalnum():
        return item + ' - alphanumeric'


def main():
    fileName = 'file.txt'
    f = open(fileName, "r")
    file_text = f.read()
    file_text = file_text[:-2]

    objects_array = file_text.split(', ')
    for item in objects_array:
        print(get_object_type(item.strip()))


main()