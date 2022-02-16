# Named Entity Recognition (NER) using BiLSTM CRF
This is a Pytorch implementation of BiLSTM-CRF for Named Entity Recognition, which is described in [Bidirectional LSTM-CRF Models for Sequence Tagging](https://arxiv.org/abs/1508.01991)

## Data
The corpus in the [data](./data) folder is MSRA Chinese NER corpus. Since there are no development data, we split the data in train.txt into training and development part when traing the model.

## Usage
For training the model, you can use the following command:
```
sh run.sh train
```
For those who are not able to use GPU, use the following command to train:
```
sh run.sh train-without-cuda
```
For testing, you can use the following command:
```
sh run.sh test
```
Also, if you have no GPU, you can use the following command(this procedure won't take long time when using CPU):
```
sh run.sh test-without-cuda
```
There is already a trained model in the [model](./model) folder, so you can execute the testing command directly without training.

If you want to change some hyper-parameters, use the following command to refer to the options.
```
python run.py --help
```

## Result
We use `custom_metric.py` to evaluate the model's performance on test data, and
the experiment result on testing data of the trained model is as follows:
```
processed 172601 tokens with 6192 phrases; found: 5660 phrases; correct: 4820.
accuracy:  97.70%; precision:  85.16%; recall:  77.84%; FB1:  81.34
              LOC: precision:  90.45%; recall:  82.31%; FB1:  86.19  2618
              ORG: precision:  78.18%; recall:  75.66%; FB1:  76.90  1288
              PER: precision:  82.38%; recall:  72.83%; FB1:  77.31  1754
```

## Reference
  1. [Bidirectional LSTM-CRF Models for Sequence Tagging](https://arxiv.org/abs/1508.01991)
  2. [cs224n Assignment 4](http://web.stanford.edu/class/cs224n/index.html#schedule)


## 补充几点：

> 这个版本可以作为bilstm+crf的baseline模型

  1. test 模型的时候，test集中的结果是不按顺序写入到结果的；
  2. 更改模型的参数配置，只需要更改docpot中的default参数即可；
  3. 模型输入的数据的格式有细微差别：是通过tab键进行分割，而不是空格；
  4. 从train、test中分别取前10000个字符加入到dev中；（总共390）

  ## 实验过程记录

  1. 任何一个新数据的训练，首先需要使用sh run.sh vocab 生成新的词表和标签表；然后使用sh run.sh train/test进行训练或测试；
