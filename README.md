## Tf-lottery

AI体彩预测：大乐透、排列3、排列5、七星彩。

## Prerequisites

- Python 3.3+
- Websocket
- TF1.X: tensorflow==1.15.3或者tensorflow-gpu==1.15.3
- [Tornado 6.0.4](https://github.com/tornadoweb/tornado)
- [Tensorflow 1.15.3](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.3)

- [LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [Aditi Mittal RNN and LSTM](https://towardsdatascience.com/understanding-rnn-and-lstm-f7cdf6dfc14e) 
- [Technical Indicators and GRU/LSTM to Predict Stock price](https://towardsdatascience.com/forecasting-with-technical-indicators-and-gru-lstm-rnn-multivariate-time-series-a3244dcbc38b)


## Directory

./data, lottery.txt rank3.txt rank5.txt starcolor.txt 体彩历届开奖数据，从体彩有记录开始截止到2020年7月

./data, input.txt Tensorflow训练时默认数据源

./save, Tensorflow训练完成之后保存的人工智能学习模型，输出预测数据时调用。该目录有已经成功训练好的体彩数据模型，可以用sample.py直接预测使用。

./tool/crash.py, 清除所有训练记录和日志方便重新开始训练 ./tool/capability.py 用于查看此计算机是否可以GPU运算以及算力大小

## Usage

train.py 用于Tensorflow深度训练学习体彩数据

--data_dir   data directory containing input.txt

--save_dir   directory to store checkpointed models

--log_dir    directory to store tensorboard logs

--rnn_size   size of RNN hidden state

--num_layers number of layers in the RNN

--model rnn, gru, lstm, or nas

--batch_size minibatch size

--seq_length RNN sequence length

--decay_rate decay rate for rmsprop

$ python train.py --save_dir save/rank3 --model lstm --batch_size 20 --save_every 500 --decay_rate 0.89 #example


sample.py 训练结束后用于输出体彩预测数据

--save_dir   model directory to store checkpointed models

--n          number of characters to sample

--prime      first lottery text

--sample     0 to use max at each timestep, 1 to sample at each timestep, 2 to sample on spaces

$ python sample.py --save_dir save/rank3 -n 200 --prime 06 --sample 1 #example

ws_server.py 启动 tornado websocket 服务端和Tensorflow训练好的模型交互


## Online Demo

[link](http://ai.workfreer.com)
