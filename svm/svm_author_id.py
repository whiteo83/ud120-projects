#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score
# X = [[0, 0], [1, 1]]
# y = [0, 1]
### Reduces the training set ####
'''
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 
print "Counts in Training Set: {}".format(len(features_train))
'''
#rint features_test
#################################

kernel_option = 'rbf'
print "Kernel Used: {}".format(kernel_option)
start = time()
clf = svm.SVC(C=10000,kernel=kernel_option,)

clf.fit(features_train, labels_train)
print "clf pred"
pred = clf.predict(features_test)
end = time()
print "clf fit & pred took {}s".format(end-start)
### print the accuracy
print "Calculating Accuracy"
print accuracy_score(pred,labels_test)
print "EOL"
#########################################################
print "Element 10 answer:{}".format(pred[10])
print "Element 26 answer:{}".format(pred[26])
print "Element 50 answer:{}".format(pred[50])
chris_count=0
for ele in pred:
    if pred[ele] == 1:
        chris_count+=1
        
print "Chris Count:{}".format(chris_count)