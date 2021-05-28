## Improving Noisy MNIST classification


### Goal
Improve the model for classifying the noisy version MNIST dataset and explain your choice of modification on a separate document with the performance results.

Make sure to include different strategies you have considered even if the performance did not change significantly. 

---

### Data

The input data has noise, while the test data are clean.

The original MNIST: [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)

Example noisy data:

**Train data**

![0](https://user-images.githubusercontent.com/5464491/119922316-8b755480-bfaa-11eb-8fa5-562193585243.png)
![1](https://user-images.githubusercontent.com/5464491/119922320-8ca68180-bfaa-11eb-9538-525cbf7d7271.png)
![2](https://user-images.githubusercontent.com/5464491/119922321-8d3f1800-bfaa-11eb-9684-efa58ca28c28.png)
![3](https://user-images.githubusercontent.com/5464491/119923083-0ee37580-bfac-11eb-9213-733c4a2fbece.png)
![4](https://user-images.githubusercontent.com/5464491/119923086-1014a280-bfac-11eb-912d-fb878029cbea.png)
![8](https://user-images.githubusercontent.com/5464491/119923088-1014a280-bfac-11eb-87ac-19f9460a90b0.png)
![9](https://user-images.githubusercontent.com/5464491/119923090-10ad3900-bfac-11eb-9721-ee8dc7e247a3.png)

**Test data**

![0](https://user-images.githubusercontent.com/5464491/119922370-a2b44200-bfaa-11eb-8a76-6bb9aed8722c.png)
![1](https://user-images.githubusercontent.com/5464491/119922375-a3e56f00-bfaa-11eb-9468-3331180e4c89.png)
![2](https://user-images.githubusercontent.com/5464491/119922376-a3e56f00-bfaa-11eb-886a-c75d8048444a.png)
![3](https://user-images.githubusercontent.com/5464491/119923009-e5c2e500-bfab-11eb-8938-42c54f31b101.png)
![4](https://user-images.githubusercontent.com/5464491/119923012-e6f41200-bfab-11eb-9bcc-de9fa5f399fe.png)
![8](https://user-images.githubusercontent.com/5464491/119923014-e6f41200-bfab-11eb-9e2d-eb97a8fa445b.png)
![9](https://user-images.githubusercontent.com/5464491/119923015-e78ca880-bfab-11eb-8932-e91c25dbbeef.png)


You may change the code in any way including the model, **except for the data itself and the transform.**

---

### What to submit
A git repo with your modifications to the provided code.
- The structure of the code may be changed in any way

A separate document, in any format, explaining different approaches considered and tested and their results.
- The results do not have to be better. However, a clear justification is prefered.
- Please include a result (table or a figure) that compares the results across different approaches.

---

**Note**
- Other repos and codes may be used, **but clear citations are required!**
- If you borrow any ideas from other literatures (e.g. blogs, papers, lectures, etc.), please make a reference to them!
