import csv

from sklearn.cluster import KMeans
import numpy as np
import random
import math


def read_csv_contents(filename):
    """Reads contents of a csv file and returns the row as a tuple
        Parameters
        -----------
        filename - string Name of the csv file
    """
    file_contents = []
    with open(filename, 'r') as fp:
        rows = csv.reader(fp)
        for row in rows:
            #  tuples are immutable
            file_contents.append(tuple(row))
    return file_contents


def categorise_dataset(contents):
	
    iris_setosa = []
    iris_versicolor = []
    iris_virginica = []
    for each_tuple in contents:
        if each_tuple[4] == 'Iris-virginica':
            iris_virginica.append(each_tuple[:4])
        elif each_tuple[4] == 'Iris-versicolor':
            iris_versicolor.append(each_tuple[:4])
        elif each_tuple[4] == 'Iris-setosa':
            iris_setosa.append(each_tuple[:4])
    sol = []

    for i in range(0,25):
    	temp = []
    	x = random.randint(0,49)
    	temp.append(iris_setosa[x])
    	x = random.randint(0,49)
    	temp.append(iris_versicolor[x])
    	x = random.randint(0,49)
    	temp.append(iris_virginica[x])
    	sol.append(temp)


    kwargs = {
        'n_init': 5,
        # depends on number of cores in your machine.
        'n_jobs': 3,
        'n_clusters': 3,
    }
    kmeans = KMeans()
    kmeans.set_params(**kwargs)
    # apply kmeans
    centroid = []
    fitness = []
    obj = []
    for x in range(0,25):
    	sol_centroid_indices = kmeans.fit_predict(np.array(sol[x]))
    	sol_centroid = kmeans.cluster_centers_
    	print sol_centroid
    	centroid.append(sol_centroid)
    	print "Solution "
    	print x
    	obj.append(compute_dist(contents,  sol_centroid))
    print "Objective Functions"
    print obj
    #return centroid

def compute_dist(contents, centroids):
	membership = []
	for each_tuple in contents:
		min_dist = 10000
		dst = 0
		for x in range(0,3):
			for y in range(0,4):
				dst= dst+((float(each_tuple[y])-centroids[x][y])*(float(each_tuple[y])-centroids[x][y]))
			dst = math.sqrt(dst)
			if(dst<min_dist):
				min_dist= dst
				pos = x
		membership.append(pos)
	print membership
	return obj_func(contents, centroids, membership)
		#print pos


def obj_func(contents, centroids, membership):
	dist = 0
	tmp = 0
	for each_tuple in contents:
		for x in range(0,4):
			dist =  dist+ ((float(each_tuple[x])-centroids[membership[tmp]][x])*(float(each_tuple[x])-centroids[membership[tmp]][x]))
		tmp= tmp + 1
	return dist

def cluster():



def optimisation():

if __name__ == '__main__':
    contents = read_csv_contents('Iris.csv')
    #centroids = 
    categorise_dataset(contents)
    #print centroids
