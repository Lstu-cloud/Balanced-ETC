import json
import os
import math
import argparse
import matplotlib.pyplot as plt
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import torch
import torch.optim as optim
import torch.nn as nn
from matplotlib.ticker import MultipleLocator
from torchvision import transforms
import torch.optim.lr_scheduler as lr_scheduler
import time
from model import shufflenet_v2_x1_0
from torchvision import transforms, datasets, models, utils

def main(args):
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")

    print(args)
    print(device)
    if os.path.exists("./weights") is False:
        os.makedirs("./weights")

    data_transform = {
        "train": transforms.Compose([transforms.RandomResizedCrop(224),
                                     transforms.RandomHorizontalFlip(),
                                     transforms.ToTensor(),
                                     transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]),
        "val": transforms.Compose([transforms.Resize(256),
                                   transforms.CenterCrop(224),
                                   transforms.ToTensor(),
                                   transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])}

    data_root = os.path.abspath(os.path.join(os.getcwd(), "../"))  # get data root path
    image_path = data_root + "/data_set/"  # flower data set path

    train_dataset = datasets.ImageFolder(root=image_path + "train",
                                         transform=data_transform["train"])
    train_num = len(train_dataset)
    print(train_num)
    flower_list = train_dataset.class_to_idx
    cla_dict = dict((val, key) for key, val in flower_list.items())
    json_str = json.dumps(cla_dict, indent=4)
    with open('class_indices.json', 'w') as json_file:
        json_file.write(json_str)

    val_dataset = datasets.ImageFolder(root=image_path + "val",
                                            transform=data_transform["val"])
    val_num = len(val_dataset)

    batch_size = args.batch_size
    nw = min([os.cpu_count(), batch_size if batch_size > 1 else 0, 8])  # number of workers
    print('Using {} dataloader workers every process'.format(nw))
    train_loader = torch.utils.data.DataLoader(train_dataset,
                                               batch_size=batch_size,
                                               shuffle=True,
                                               pin_memory=True,
                                               num_workers=nw,
                                               #collate_fn=train_dataset.collate_fn
                                               )

    val_loader = torch.utils.data.DataLoader(val_dataset,
                                             batch_size=batch_size,
                                             shuffle=False,
                                             pin_memory=True,
                                             num_workers=nw,
                                             #collate_fn=val_dataset.collate_fn
                                             )

    model = shufflenet_v2_x1_0(num_classes=args.num_classes).to(device)

    model.to(device)

    pg = [p for p in model.parameters() if p.requires_grad]

    optimizer = optim.SGD(pg, lr=args.lr, momentum=0.9, weight_decay=4E-5)
    lf = lambda x: ((1 + math.cos(x * math.pi / args.epochs)) / 2) * (1 - args.lrf) + args.lrf  # cosine
    scheduler = lr_scheduler.LambdaLR(optimizer, lr_lambda=lf)
    loss_function = nn.CrossEntropyLoss()
    best_acc = 0
    save_path = 'class918.pth'
    train_acc, train_loss1, test_acc, test_loss, epochs = [], [], [], [], []
    sumtime = 0
    time_sum = []
    average = []

    for i in range(1):
        for epoch in range(5):
            model.train()
            running_loss = 0
            total_val_loss = 0
            acc1 = 0
            time1 = time.time()
            for step, data in enumerate(train_loader, start=0):
                images, labels = data
                optimizer.zero_grad()
                logits = model(images.to(device))
                loss = loss_function(logits, labels.to(device))
                loss.backward()
                optimizer.step()
                running_loss += loss.item()
                predict_y = torch.max(logits, dim=1)[1]
                acc1 += (predict_y == labels.to(device)).sum().item()
                rate = (step + 1) / len(train_loader)
                a = "*" * int(rate * 50)
                b = "." * int((1 - rate) * 50)
                print("\rtrain loss: {:^3.0f}%[{}->{}]{:.4f}".format(int(rate * 100), a, b, loss), end="")
            print()
            train_accurate = acc1 / train_num
            train_loss = running_loss / len(train_loader)
            epochs.append(epoch)
            train_acc.append(train_accurate)
            train_loss1.append(train_loss)
            # validate
            model.eval()
            acc = 0

            with torch.no_grad():
                for val_data in val_loader:
                    val_images, val_labels = val_data
                    outputs = model(val_images.to(device))
                    loss = loss_function(outputs, val_labels.to(device))
                    total_val_loss += loss.item()
                    predict_y = torch.max(outputs, dim=1)[1]
                    acc += (predict_y == val_labels.to(device)).sum().item()
                val_accurate = acc / val_num
                ave_loss_val = total_val_loss / len(val_loader)
                if val_accurate > best_acc:
                    best_acc = val_accurate
                    torch.save(model.state_dict(), save_path, _use_new_zipfile_serialization=False)
                print('[epoch %d] train_loss: %.4f  test_accuracy: %.4f' %
                      (epoch + 1, running_loss / step, val_accurate))
                time2 = time.time()

                test_acc.append(val_accurate)
                test_loss.append(ave_loss_val)

            sumtime = sumtime + (time2 - time1)
            time_sum.append(sumtime)
            average.append(best_acc)
        print("\rsumtime: %.4f" % sumtime)
        print("ACC:%.4f" % best_acc)

        plt.plot(epochs, test_acc, "b.-", label='test_acc')
        plt.plot(epochs, test_loss, "r-", label='test_loss')

        plt.xlabel('epoch')
        plt.ylabel('Accuracy', )

        plt.legend()
        y_major_locator = MultipleLocator(0.1)
        x_major_locator = MultipleLocator(5)
        ax = plt.gca()
        ax.xaxis.set_major_locator(x_major_locator)
        ax.yaxis.set_major_locator(y_major_locator)
        plt.ylim(0, 1)
        plt.xlim(0, 50)

        plt.savefig(r'C:\321\Processing_classification\Processing_classification\Processing_classification\line\class.jpg')
        plt.show()

    print('Finished Training')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_classes', type=int, default=14)
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--batch-size', type=int, default=16)
    parser.add_argument('--lr', type=float, default=0.01)
    parser.add_argument('--lrf', type=float, default=0.1)
    parser.add_argument("--freeze-layers", type=bool, default=False)
    parser.add_argument('--device', default='cuda:0', help='device id (i.e. 0 or 0,1 or cpu)')

    opt = parser.parse_args()

    main(opt)
