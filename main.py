print('Imports starting')
from keras.datasets import imdb   
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from keras.preprocessing.sequence import sequence

print('Starting script')
max_words = 10000

maxlen = 32

(x_train, y_train), (_, _) = imdb.load_data(num_words=max_words)

print(x_train[:2])

x_train = sequence.pad_sequences(x_train, maxlen=maxlen)

print(y_train[:10])

model = Sequential()
model.add(Embedding(max_words, 16))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))
