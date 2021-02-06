try:
    file = open('new.txt')
    file.close()
except FileNotFoundError:
    print("Такого файла не существует")