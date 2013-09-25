from __future__ import division
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
    
# Import the data
iris=datasets.load_iris()
iris_x=iris.data
iris_y=iris.target
print np.unique(iris_y)

#Divide the data for cross-validation
def nFoldSplit(n,iris_x,iris_y,iris_x_train,iris_y_train,iris_x_test,iris_y_test):
        np.random.seed(0)  #randomize the data rows
        indices=np.random.permutation(len(iris_x)) #len(iris_x)= 150
        iris_x_train=iris_x[indices[:-math.trunc((len(iris_x)/n))]]
        iris_y_train=iris_x[indices[:-math.trunc((len(iris_y)/n))]]
        iris_x_test=iris_x[indices[math.trunc((len(iris_x)/n)):]]
        iris_y_test=iris_x[indices[math.trunc((len(irix_y)/n)):]]
        return iris_x_test,iris_y_test,iris_x_train,iris_y_train

#call the split function

nFoldSplit(10,iris_x,iris_y,iris_x_train,iris_y_train,iris_x_test,iris_y_test)

# Create the classifier

results=[ ]
for n in enumerate(iris_X_train):
	knn = KNeighborsClassifier(n_neighbors=n)
	knn.fit(iris_X_train,iris_Y_train)
	prediction=knn.predict(iris_X_test)
	#return the predicted results
	accuracy=np.where(prediction==iris_X_test,1,0).sum()/float(len(iris_X_test))
	print "Neighbors: %d, Accuracy: %3f" % (n, accuracy)
	results.append([n,accuracy])
results=pd.DataFrame(results,columns=["n","accuracy"])

print results

