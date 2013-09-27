from __future__ import division
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation

# Import the data
iris=datasets.load_iris()
iris_x=iris.data
iris_y=iris.target
#print np.unique(iris_y)

#Divide the data for validation

k = [5, 15]
SEED = 42
n = 10
def nFoldSplit(k):#n,iris_x,iris_y,iris_x_train,iris_y_train,iris_x_test,iris_y_test):
	for i in range(n):
		iris_x_train, iris_x_test, iris_y_train, iris_y_test = cross_validation.train_test_split(iris_x, iris_y, test_size=0.2, random_state=i*SEED)

#Create the classifier and fit a model to it
		knn = KNeighborsClassifier(n_neighbors=k)
		knn.fit(iris_x_train,iris_y_train)
		iris_y_prediction=knn.predict(iris_x_test)
#Calculate the accuracy of the model
		accuracy = knn.score(iris_x_test, iris_y_test)
		#accuracy=np.where(prediction==iris_X_test,1,0).sum()/float(len(iris_X_test))
		print "Neighbors: %d, Accuracy: %3f" % (k, accuracy)
	print np.average(accuracy)
	print "Average accuracy: " + str(np.average(accuracy)) + "% over " + str(n) + " runs"

print nFoldSplit(5)

