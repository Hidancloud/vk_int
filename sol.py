import random

epsilon = 10**(-3)

def dist_euclidian_1d(x, y):
    return abs(x - y)


def sort_first(arr):
    return arr[0]


def precalc(inp, metric):
    eps = []
    for index, item in enumerate(inp):
        if index == len(inp) - 1:
            break
        eps.append([metric(item, inp[index+1]), index])
    eps.sort(key=sort_first)
    return eps


def h_clustering_1d(raw_data):
    data = raw_data
    data.sort()
    history = []
    clusters = [i for i in range(len(data))]
    history.append([clusters.copy(), float('inf')])
    distances = precalc(data, dist_euclidian_1d)
    # print(distances)
    # print("TEST:")
    for i in range(len(data)-1):
        # print(clusters)
        #1st step is to merge
        j = 1
        x = clusters[distances[0][1] + 1]
        while j + distances[0][1] < len(clusters) and (clusters[distances[0][1] + j] == x):
            clusters[distances[0][1] + j] = clusters[distances[0][1]]
            j += 1
        history.append([clusters.copy(), distances[0][0]])
        #2nd step is to remove first distance instance
        del distances[0]
    return history


def decision(hist):
    ans = []
    max_split = -float('inf')
    for ind, h in enumerate(hist):
        if ind == len(hist) - 1:
            break
        if hist[ind + 1][1] - hist[ind][1] > max_split:
            ans = hist[ind]
            max_split = hist[ind + 1][1] - hist[ind][1]
    # some cosmetic changes
    ann = ans[0]
    max  = ann[0]
    for i, el in enumerate(ann):
        if el > max+1:
            max += 1
            ann[i] = max
    return [ann, ans[1]]


maxnumber = 10
size = 20
random.seed(10)
points = [random.uniform(0, maxnumber) for x in range(size)]
points.sort()
answer = h_clustering_1d(points)
result = decision(answer)
print("points:")
print(points)
print("clusters:")
print(result[0])
print("with optimal distance chosen:")
print(result[1])
