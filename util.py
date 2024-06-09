import numpy as np
from matplotlib import pyplot as plt

def show_im(i, text = "Image"):
    if type(i) == type([]):
        print(text)
        fig, axes = plt.subplots(1, len(i), figsize=(20, 4))
        index = 221
        for j in range(len(i)):
            dim0 = str(i[j].shape[0]) 
            dim1 = str(i[j].shape[1])
            title = text[j] + " : " + dim0 + "x" + dim1
            # print(title, dim0, dim1)
            axes[j].imshow(i[j], cmap=plt.get_cmap('gray'))
            # axes[j].title(title)
            # axes[j].xticks([])
            # axes[j].yticks([])
    else: 
        plt.imshow(i, cmap=plt.get_cmap('gray'))
        plt.title(text + ': ' + str(i.shape[0]) + ", " + str(i.shape[1]) )
        plt.xticks([])
        plt.yticks([])
        plt.show()
