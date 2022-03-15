# 2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# под форматами понимаем структуру файлов, например:
# - в файле на одной строке хранится одна часть записи, пустая строка - разделитель
#
# Фамилия_1
# Имя_1
# Телефон_1
# Описание_1
#
# Фамилия_2
# Имя_2
# Телефон_2
# Описание_2
#
# и т.д.
# - в файле на одной строке хранится все записи, символ разделитель - ;
# Фамилия_1,Имя_1,Телефон_1,Описание_1
# Фамилия_2,Имя_2,Телефон_2,Описание_2
#
# Использовать CSV(Если есть желание, можно попробовать возможность чтения XML)







a = input('Фамилия: ')
b = input('Имя: ')
c = input('Телефон +')
d = input('Описание: ')
# # str(input('Фамилия: ')),str(input('Имя: ')),int(input('Телефон: ')),str(input('Описание: '))

if a.isalpha() == False:
    exit()
if b.isalpha() == False:
    exit()

if c.isnumeric() == False:
    exit()

def inputUsers(surname,name,tel,comment):
    
    list = [surname,name,tel,comment]        
    list1 = ' '.join(list)
    return list1

def inputUsers2(surname,name,tel,comment):     
    
    list = [surname,name,tel,comment]        
    list1 = '\n'.join(list)
    return list1
    
with open('file1.csv', 'a') as data:
    data.writelines(inputUsers(a,b,c,d))
    data.write('\n')

with open('file2.csv', 'a') as data:
    data.write('\n')
    data.writelines(inputUsers2(a,b,c,d))
    
while format != 1 or format != 2:
    format = int(input('Выбирите формат вывода 1 или 2?: '))
    if format == 1:
        path = 'file1.csv'
        data = open(path, 'r')
        for line in data:
            print(line)
    elif format == 2:
        path = 'file2.csv'
        data = open(path, 'r')
        for line in data:
            print(line)