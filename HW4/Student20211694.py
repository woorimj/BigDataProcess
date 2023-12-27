import sys
import numpy as np
import os
import operator


# 숫자 데이터를 읽어오기
def load_digits(filename):
    labels = []
    trainList = os.listdir(filename)
    l = len(trainList)
    matrix = np.zeros((l, 1024))

    for i in range(l):
        t = trainList[i]
        result = int(t.split("_")[0])
        labels.append(result)
        matrix[i, :] = reshape_data(filename + "/" + t)

    return matrix, labels


# 거리계산
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True
    )

    return sortedClassCount[0][0]


# 이미지 픽셀값 -> 2차원 배열로변경
def reshape_data(filename):
    reshape_data = np.zeros((1, 1024))
    with open(filename) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                reshape_data[0, 32 * i + j] = int(line[j])
        return reshape_data


# trainingDigits와 testDigits로부터 숫자 데이터 읽기
trainFile = sys.argv[1]
testFile = sys.argv[2]
testList = os.listdir(testFile)
matrix, labels = load_digits(trainFile)

for k in range(1, 21):
    file_count = 0
    error_count = 0
    for i in range(len(testList)):
        result = int(testList[i].split("_")[0])
        test_data = reshape_data(testFile + "/" + testList[i])
        classify = classify0(test_data, matrix, labels, k)

        file_count += 1
        if result != classify:
            error_count += 1

    error_rate = (error_count / file_count) * 100
    print(f"K = {k}일 때는 {int(error_rate)}%")
