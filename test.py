import pandas as pd

print(f"{'*' * 20}\nStarting script...\n{'*' * 20}")

base_materials_path = '/home/jaims/zheka/diplomNeuro/materials/'
positive_path = f'{base_materials_path}/positive.csv'
test_path = f'{base_materials_path}/test.csv'


def blockPrint(msg: str) -> None:
    
    print(f"{'*' * 20}\n{msg}\n{'*' * 20}")

blockPrint('Start reading data...')
data_raw = pd.read_csv(test_path, error_bad_lines=False)
print('successfully readed data from csv file!')

blockPrint('DataFrame initializing')
# создаем DataFrame из считанных данных
data = pd.DataFrame(data = data_raw)

# показывем немного считанных данных в консоль
first_ten = data.head(10)
t = data.iloc[0]
print(first_ten)
print(t)


