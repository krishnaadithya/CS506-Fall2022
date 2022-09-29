import numpy as np
from numpy.linalg import norm

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):

    return return sum(abs(val1-val2) for val1, val2 in zip(x,y))

def jaccard_dist(x, y):

    if np.unique(x) == [0,1] and np.unique(y) == [0,1]:
    
        intersection = np.logical_and(x, y)
        union = np.logical_or(x, y)
        similarity = intersection.sum() / float(union.sum())
        distance = 1- similarity
    
    else: 
        intersection = len(list(set(x).intersection(y)))
        union = (len(x) + len(y)) - intersection
        distance = float(intersection) / union

    return distance

def cosine_sim(x, y):

    return np.dot(A,B)/(norm(A)*norm(B))

# Feel free to add more
