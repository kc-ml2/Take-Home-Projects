import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision.utils as utils
import torchvision.datasets as datasets
import torchvision.transforms as transforms


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


################## Do not modify the code in this area #######################

class RandomNoise(object):
    def __init__(self, prob=0.5, noise_level=0.5):
        self.prob = prob
        self.noise_level = noise_level

    def __call__(self, tensor):
        mask = (torch.rand_like(tensor) < self.noise_level).float()
        noise = torch.rand_like(tensor)
        if torch.rand(1)[0] < self.prob:
            return mask * noise + (1 - mask) * tensor
        else:
            return tensor

    def __repr__(self):
        return (self.__class__.__name__
                + '(prob={0}, std={1})'.format(self.prob, self.noise_level))


def train(model, train_loader, loss_func, optimizer, epoch, log_interval):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = loss_func(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Epoch {} [{}/{}]: Loss{:6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset), loss))

def test(model, test_loader, loss_func):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += loss_func(output, target).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)

    print('\nTest set: Average loss: {:4f}, Accuracy: {}/{} ({:.0f}%)'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))

def save_image(dataset, key='data'):
    import matplotlib
    matplotlib.use('TkAgg')
    from matplotlib import pyplot as plt
    import os
    os.makedirs('images/{}'.format(key), exist_ok=True)

    for i in range(10):
        image, label = dataset[i]
        plt.imsave(
            'images/{}/{}.png'.format(key, i),
            image.squeeze().cpu().numpy(),
            cmap='gray')
        plt.close()


transform_train = transforms.Compose([
    transforms.ToTensor(),
    RandomNoise(1.0, 0.7),
    transforms.Normalize((0.1307,), (0.3081))
])

transform_test = transforms.Compose([
    transforms.ToTensor(),
    RandomNoise(0.0, 0.5),
    transforms.Normalize((0.1307,), (0.3081))
])

train_set = datasets.MNIST(root='data/', train=True,
                           transform=transform_train, download=True)
test_set = datasets.MNIST(root='data/', train=False,
                          transform=transform_test, download=True)

# save_image(train_set, 'train')
# save_image(test_set, 'test')

#################### Anything below can be modified ##########################


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(28 * 28, 32),
            nn.Sigmoid(),
            nn.Linear(32, 32),
            nn.Sigmoid(),
            nn.Linear(32, 10)
        )

    def forward(self, x):
        x = x.view(-1, 28*28)
        x = self.mlp(x)
        return F.log_softmax(x, dim=1)

train_batch = 16
lr = 1e-2
epochs = 10
loss_func = F.nll_loss
log_interval = 100

train_loader = torch.utils.data.DataLoader(train_set, batch_size=train_batch)
test_loader = torch.utils.data.DataLoader(test_set, batch_size=1000)

model = Model().to(device)
optimizer = optim.SGD(model.parameters(), lr=1e-3)

for epoch in range(1, epochs):
    train(model, train_loader, loss_func, optimizer, epoch, log_interval)
    test(model, train_loader, loss_func)
