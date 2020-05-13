import numpy as np
import random
from sklearn import svm
from sklearn.datasets import load_iris

print("----- Classifying IRIS flower with sklearn using LibSVM  ----")
iris = load_iris()  # contains 3 classes, 150 samples with 4 features

# Index samples by class
zippedY2X = {} # indexed data: class (y) -> list of samples (X)
for x, y in zip(iris.data, iris.target):
    if not y in zippedY2X:
        zippedY2X[y] = []
    zippedY2X[y].append(x)

# Shuffle samples; then split data and take 70% for training, 30% for test
trainingSamplesCount = int(0.7 * len(zippedY2X[zippedY2X.keys()[0]]))
trainingY2X = {}
testY2X = {}
print("Total Samples per class: {s} - Training: {o} - Test: {t}"
        .format(s=len(zippedY2X[zippedY2X.keys()[0]]), 
        o=trainingSamplesCount,
        t=len(zippedY2X[zippedY2X.keys()[0]])-trainingSamplesCount))
for y in zippedY2X.keys():
    random.shuffle(zippedY2X[y])
    trainingY2X[y] = zippedY2X[y][:trainingSamplesCount]    #70% 
    testY2X[y] = zippedY2X[y][trainingSamplesCount:]        #30%

compiledTrainingData = { 'samples': [], 'targets': [] }
for y in trainingY2X.keys():
    compiledTrainingData['samples'].extend(trainingY2X[y]) 
    Y =  [ [y] for i in range(len( trainingY2X[y]))]
    compiledTrainingData['targets'].extend(Y) 

print("Training Data: Samples: {s} - Targets: {t}"
    .format(s=len(compiledTrainingData['samples']), 
    t=len(compiledTrainingData['targets'])))

# Build SVM and feed compiled training data into it
clf = svm.SVC(kernel='poly', gamma=0.5)
clf.fit(    compiledTrainingData['samples'], 
            np.asarray(compiledTrainingData['targets']).ravel() )

for y, X in testY2X.items():
    p_y = clf.predict(X)
    print("Predicted {py} for actual target {at}".format(py = p_y, at = y))
