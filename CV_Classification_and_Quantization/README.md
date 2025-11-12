# **Take Home Project**

**Submission Deadline:** 2025/11/19 23:59 KST  

---

## **Objective**

The goal of this assignment is to design, train, and optimize a small convolutional neural network (CNN) for 10-class classification, and then apply model quantization techniques to reduce model size and improve inference efficiency. You will evaluate how quantization impacts model accuracy, size, and speed.

---

## **Tasks**

### **Part 1: Data Preparation**

- Use a small publicly available dataset such as **CIFAR10** *(preferred)* or MNIST.  
- Preprocess the data: resize images, normalize pixel values.  
- Properly utilize training, validation, and test splits.  



### **Part 2: Model Design and Training**

- Implement a compact CNN using **PyTorch** *(preferred)* or any other platform like TensorFlow/Keras.  
- Train the model.  
- Report:
  - Model architecture summary.  
  - Training and validation accuracy/loss curves.  
  - Final test accuracy.  


### **Part 3: Model Quantization**

- Apply **post-training quantization (PTQ)** using PyTorch’s quantization toolkit or TensorFlow Lite.  
- Compare:
  - Model file size before vs. after quantization.  
  - Inference time on CPU.  
  - Accuracy difference after quantization.  
  - **NOTE:** At least one quantization precision is required. More are encouraged for extra credit.  


### **Part 4: Analysis and Discussion**

- Write a short (1–2 page) analysis addressing:
  - The effect of quantization on model performance and accuracy.  
  - Trade-offs between compression and precision.  
  - Benefits of deploying quantized models on edge devices.  

---

## **Deliverables**
 - A github link to a repo containing
    - Jupyter Notebook or Python script that includes preprocessing, model training, and quantization.  
    - A 1–2 page written analysis report from Part 4.  

