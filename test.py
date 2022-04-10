import pandas as pd
print('Started script')

p = '/home/jaims/zheka/diplomNeuro/materials/positive.csv' 
p_test = '/home/jaims/zheka/diplomNeuro/materials/test.csv' 
print('Start reading data...')
data_raw = pd.read_csv(p, error_bad_lines=False)
print('data readed')
data = pd.DataFrame(data = data_raw)
first_ten = data.head(10)
t = data.iloc[0]
print(t)
# seems like nothing new appeared
