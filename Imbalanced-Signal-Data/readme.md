# Imbalanced Signal Data

## Project Outline
The aim of this project is to resolve a dataset problem of imbalance.

The dataset is about Arrhythmia, which is a heart disease and can be detected by ECG(heartbeat) signal.

The problem in the data is that Normal and abnormal data data are largely biased(Mostly normal). Abnormal data have multiple types each having small data number.

This deteriorates the classfication problem to detect patients from the signal.

Original way of solving this problem was to set the number of each dataset to the dataset with minimum number.

But this way implied a large waste of unused data.

Here, you are asked to solve the prolbem by oversampling the data.


## DataSet
[preprocessed ECG Heartbeat Dataset](https://www.kaggle.com/shayanfazeli/heartbeat)

Use the mit-bih dataset named 'mitbih_test.csv' and 'mitbih_train.csv'.


## Data Infomation

Number of Samples: 109446

Number of Categories: 5

Sampling Frequency: 125Hz

Data Source: [Physionet's MIT-BIH Arrhythmia Dataset](https://www.physionet.org/content/mitdb/1.0.0/)

Classes: ['N': 0, 'S': 1, 'V': 2, 'F': 3, 'Q': 4]

Data Number: ['N': 90590, 'S': 2889, 'V': 7278, 'F': 4308, 'Q': 8084]




## Performance Check

Convnet1D

RNN



## Hints

What you can refer to: [7 Over Sampling techniques to handle Imbalanced Data](https://towardsdatascience.com/7-over-sampling-techniques-to-handle-imbalanced-data-ec51c8db349f?gi=8670a501d3c3)
