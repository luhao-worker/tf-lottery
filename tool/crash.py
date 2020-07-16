import shutil
import os
file_data = 'data/data.npy'
file_vocab = 'data/vocab.pkl'
if os.path.exists(file_data):
    os.remove(file_data)
if os.path.exists(file_vocab):
    os.remove(file_vocab)
if os.path.exists('__pycache__'):
    shutil.rmtree('__pycache__')
if os.path.exists('logs'):
    shutil.rmtree('logs')
if os.path.exists('save'):
    shutil.rmtree('save')
if os.path.exists('__pycache__') == False:
    os.mkdir('__pycache__')
if os.path.exists('logs') == False:
    os.mkdir('logs')
if os.path.exists('save') == False:
    os.mkdir('save')
print('clean ok!')

