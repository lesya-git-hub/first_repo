#Функція get_cats_info(path) приймає один аргумент - шлях до текстового файлу (path).
#Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
#Функція повертає список словників, де кожен словник містить інформацію про одного кота.

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
           for line in file:
               try:
                   cats_id, cats_name, cats_age = line.strip().split(',')
                   cats_dict = {
                       'id': cats_id,
                       'name': cats_name,
                       'age': cats_age
                   }
                   cats_info.append(cats_dict)
               except ValueError:
                   print("Помилка: ", line)
           return cats_info
    except FileNotFoundError:
        print("File not found, please check the path to the file")
        return []
cats_info = get_cats_info("cats_file.txt")
for cat in cats_info:
    print(cat)

