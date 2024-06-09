import numpy as np

def median(patch):
    dim = patch.shape[0] * patch.shape[1]
    arr = patch.reshape(1, dim)
    arr = np.sort(arr)

    if(dim % 2 == 0):
        median = arr[0][dim/2]
    else:
#         print(arr[0][dim//2], arr[0][(dim//2) + 1])
        median = (arr[0][dim//2] + arr[0][(dim//2) + 1]) / 2

    return median


def mean(patch):
    return np.mean(patch)


def variance(patch):
    N = patch.shape[0] * patch.shape[1]
    u = np.mean(patch)
    var = np.sum((patch - u) ** 2)
    return var / (N - 1)

def std_dev(patch):
    u = np.mean(patch)
    var = np.mean((patch - u) ** 2)
    return np.sqrt(var)

def skewness(patch):
    sigma = std_dev(patch)
    u = np.mean(patch)
    skew = np.mean(((patch - u) ** 3/ sigma ** 3))
    return skew         

def kurtosis(patch):
    sigma = std_dev(patch)
    u = np.mean(patch)
    skew = np.mean(((patch - u) ** 4/ sigma ** 4))
    return skew         

def mad(patch):
    u = np.mean(patch)
    val = np.mean((patch - u))
    return val

def mead(patch):
    m = mad(patch)
    y = patch - m
    dim = patch.shape[0] * patch.shape[1]
    arr = patch.reshape(1, dim)
    arr = np.sort(arr)

    if(dim % 2 == 0):
        median = arr[0][dim/2]
    else:
#         print(arr[0][dim//2], arr[0][(dim//2) + 1])
        median = (arr[0][dim//2] + arr[0][(dim//2) + 1]) / 2

    return median

def local_contrast(patch):
    h = np.max(patch)
    l = np.min(patch)
    return h - l

def local_probablities(patch, k=178):
#     print(np.sum(patch == gray_level), " << ")
    return (np.sum(patch == k))

def percetile(patch, percent=0.75):
    dim = patch.shape[0] * patch.shape[1]
    arr = patch.reshape(1, dim)
    arr = np.sort(arr)
    
    N = len(arr)
    rank = percent * (N + 1)
    
    if not rank.is_integer():
        rank = int(rank) - 1
    
    return arr[0][rank]    


def percetile_25(patch):
    return percetile(patch, 0.25)

def percetile_75(patch):
    return percetile(patch, 0.75)