"""
    Учись верно оформлять файл, не стесняйся хороших принтов и 
    комментариев
"""
import pandas as pd

"""
    С помощью f перед строкой (format) возможно внутрь строки передавать
    переменные / какой-то код в {} скобках, это используется довольно часто 
    помощью f перед строкой (format) возможно внутрь строки передавать
    переменные / какой-то код в {} скобках, это используется довольно часто,
    вот пример
"""

print(f"{'*' * 20}\nStarting script...\n{'*' * 20}")

"""
    Данная запись принта даст такой результат, разберись, почему

    ********************
    Starting script...
    ********************

"""

# Как было бы лучше сделать переменные путей и затем подставлять:
base_materials_path = '/home/jaims/zheka/diplomNeuro/materials/'
positive_path = f'{base_materials_path}/positive.csv'
test_path = f'{base_materials_path}/test.csv'
# Посмотри на вариант ниже и замени на этот

p = '/home/jaims/zheka/diplomNeuro/materials/positive.csv' 
p_test = '/home/jaims/zheka/diplomNeuro/materials/test.csv' 


"""
    Почему бы не создать классный метод для кул принта в консоль
    сообщений, которые разделяют важные блоки кода.
    Показываю, чтобы у тебя было +1 к креативу, динамичному мышлению,
    как ты можешь применять функционал языка и облегчать себе жизнь
"""
def blockPrint(msg: str) -> None:
    """
        Метод для красивой печати сообщения, которое логически разделяет
        выполняемые блоки кода между собой.
    """
    # Итак, просто скопировал принт выше, но теперь принт будет работать
    # с динамической переменной msg, что ты дальше будешь передавать
    print(f"{'*' * 20}\n{msg}\n{'*' * 20}")


# пора заюзать cозданный метод
# старая версия - print('Start reading data...')
blockPrint('Start reading data...')
# считываешь данные, игнорируем строки с некорректных форматом данных
data_raw = pd.read_csv(p, error_bad_lines=False)
print('successfully readed data from csv file!')

blockPrint('DataFrame initializing')
# создаем DataFrame из считанных данных
data = pd.DataFrame(data = data_raw)

# показывем немного считанных данных в консоль
first_ten = data.head(10)
t = data.iloc[0]
print(first_ten)
print(t)

blockPrint('Script finished! ٩(◕‿◕｡)۶')
