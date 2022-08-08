## Imbalanced Signal Data


### Goal

The aim of this project is to solve classification problem. This dataset's class distribution is imbalanced.

The dataset is about Arrhythmia, which is a heart disease and can be detected by ECG(heartbeat) signal. The problem in the data is that normal and abnormal data data are largely biased(Mostly normal). Abnormal data have multiple types each having small data number. This deteriorates the classfication problem to detect patients from the signal.

Original way of solving this problem was to set the number of each dataset to the dataset with minimum number. But this way implied a large waste of unused data.

Here, you are asked to solve the problem by oversampling the data.

---

### Data


[Preprocessed ECG Heartbeat Dataset](https://www.kaggle.com/shayanfazeli/heartbeat)

Use the mit-bih dataset named **mitbih_test.csv** and **mitbih_train.csv**.


Number of Samples: 109446

Number of Categories: 5

Sampling Frequency: 125Hz

Classes: ['N': 0, 'S': 1, 'V': 2, 'F': 3, 'Q': 4] (N: normal, others: abnormal types)

---

### What to submit
A git repo with your code.

A separate document, in any format, explaining your approach and results.

---

**Note**
- Other repos and codes may be used, **but clear citations are required!**
- If you borrow any ideas from other literatures (e.g. blogs, papers, lectures, etc.), please make a reference to them!
- You may refer to: [7 Over Sampling techniques to handle Imbalanced Data](https://towardsdatascience.com/7-over-sampling-techniques-to-handle-imbalanced-data-ec51c8db349f?gi=8670a501d3c3)
