# MachineLearning101: sklearn_iris_svm.py

sklearn_iris_svm.py is an easy example for demonstrating how to use a SVM (Support Vector Machine) with python.

As of today, sklearns SVM is a wrapper for LibSVM. LibSVM is a binary tool with a nice command line interface (https://www.csie.ntu.edu.tw/~cjlin/libsvm/). 

The iris data is the famous Fisher dataset: https://en.wikipedia.org/wiki/Iris_flower_data_set 

Natively, vanilly SVMs only support binary classification. LibSVM however implements a Multiclass extension using modified equations. So LibSVMs Multiclass approach implements a logic that may not be the optimal strategy for your multiclass problem. Do you train one binary classifier per class? For each class, different features maybe decisive. Take into account classifying emails into folders: Some folders or tags are about persons, some about years, some about topics, some about importance...
https://en.wikipedia.org/wiki/Ensemble_learning

Requirements:
python 3
pip install sklearn


