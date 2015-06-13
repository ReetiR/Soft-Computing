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
    obj = []
    for x in range(0,25):
    	print "Solution "
    	print x
    	print sol[x]
    	obj.append(compute_dist(contents,  sol[x]))
    print "Objective Functions"
    print obj
    centroid = cluster(sol, obj)
    opti_algo(centroid)
    #return centroid

def compute_dist(contents, centroids):
	membership = []
	for each_tuple in contents:
		min_dist = 10000
		dst = 0
		for x in range(0,3):
			for y in range(0,4):
				dst= dst+((float(each_tuple[y])-float(centroids[x][y]))*(float(each_tuple[y])-float(centroids[x][y])))
			dst = math.sqrt(dst)
			if(dst<min_dist):
				min_dist= dst
				pos = x
		membership.append(pos)
	#print membership
	return obj_func(contents, centroids, membership)
		#print pos


def obj_func(contents, centroids, membership):
	dist = 0
	tmp = 0
	for each_tuple in contents:
		for x in range(0,4):
			dist =  dist+ ((float(each_tuple[x])-float(centroids[membership[tmp]][x]))*(float(each_tuple[x])-float(centroids[membership[tmp]][x])))
		tmp= tmp + 1
	return dist

def cluster(centroids, obj):
	new_set = []
	prev_min = 0
	pos= 0
	for x in range(0,25):
		min_val = 1000
		for y in range(0,25):
			if (obj[y]< min_val) and (obj[y]>prev_min):
				min_val = obj[y]
				pos = y
		prev_min = obj[pos]
		print pos
		new_set.append(centroids[pos])
	return new_set

def opti_algo(centroids):
	centroid_rep1= []
	rep2= []
	size1= random.randint(2, 7)
	size2= random.randint(2, 7)
	size3= random.randint(2, 7)
	size4= random.randint(2, 7)
	size5= 25 - (size1+size2+size3+size4)
	num = random.random()
	p_replace = 0.2
	p_one = 0.8
	p_one_center = 0.4
	p_two_center = 0.5
	if(num<p_replace):
		n=  random.randint(0, 4)
		centroid_rep1[0][0][0]= random.uniform(4.3,5.8)
		centroid_rep1[0][0][1]= random.uniform(2.3,4.4)
		centroid_rep1[0][0][2]= random.uniform(1,1.9)
		centroid_rep1[0][0][3]= random.uniform(0.1,0.6)
		centroid_rep1[0][1][0]= random.uniform(4.9,7)
		centroid_rep1[0][1][1]= random.uniform(2,3.4)
		centroid_rep1[0][1][2]= random.uniform(3,5.1)
		centroid_rep1[0][1][3]= random.uniform(1,1.8)
		centroid_rep1[0][2][0]= random.uniform(4.9,7.9)
		centroid_rep1[0][2][1]= random.uniform(2.2,3.8)
		centroid_rep1[0][2][2]= random.uniform(4.5,6.9)
		centroid_rep1[0][2][3]= random.uniform(1.4,2.5)
	for x in range(0,25):
		num = random.random()
		if(num<p_one):
			num =  random.random()
			if (size1>size2) and (size1>size3) and (size1>size4) and (size1>size4) and (size1>size5):
				center = 0
				rand1 = random.randint(0,size1-1)
				rand2= random.randint(0,size1-1)
			elif (size2>size3) and (size2>size4) and (size2>size5):
				center = size1
				rand1 = random.randint(size1,size1+size2-1)
				rand2= random.randint(size1,size1+size2-1)
			elif (size3> size4) and (size3>size5):
				center = size1+size2
				rand1 = random.randint(size1+size2, size1+size2+size3-1)
				rand2= random.randint(size1+size2, size1+size2+size3-1)
			elif (size4>size5):
				center = size1+size2+size3
				rand1 = random.randint(size1+size2+size3, size1+size2+size3+size4-1)
				rand2= random.randint(size1+size2+size3, size1+size2+size3+size4-1)
			else:
				center = size1+size2+size3+size4
				rand1 = random.randint(size1+size2+size3+size4, 24)
				rand2= random.randint(size1+size2+size3+size4, 24)
			if(num<p_one_center):
				rep2[0][0][0] = centroids[center][0][0] + (random.random()*(centroids[rand1][0][0]-centroids[rand2][0][0]))
				rep2[0][0][1] = centroids[center][0][1] + (random.random()*(centroids[rand1][0][1]-centroids[rand2][0][1]))
				rep2[0][0][2] = centroids[center][0][2] + (random.random()*(centroids[rand1][0][2]-centroids[rand2][0][2]))
				rep2[0][0][3] = centroids[center][0][3] + (random.random()*(centroids[rand1][0][3]-centroids[rand2][0][3]))
				rep2[0][1][0] = centroids[center][1][0] + (random.random()*(centroids[rand1][1][0]-centroids[rand2][1][0]))
				rep2[0][1][1] = centroids[center][1][1] + (random.random()*(centroids[rand1][1][1]-centroids[rand2][1][1]))
				rep2[0][1][2] = centroids[center][1][2] + (random.random()*(centroids[rand1][1][2]-centroids[rand2][1][2]))
				rep2[0][1][3] = centroids[center][1][3] + (random.random()*(centroids[rand1][1][3]-centroids[rand2][1][3]))
				rep2[0][2][0] = centroids[center][2][0] + (random.random()*(centroids[rand1][2][0]-centroids[rand2][2][0]))
				rep2[0][2][1] = centroids[center][2][1] + (random.random()*(centroids[rand1][2][1]-centroids[rand2][2][1]))
				rep2[0][2][2] = centroids[center][2][2] + (random.random()*(centroids[rand1][2][2]-centroids[rand2][2][2]))
				rep2[0][2][3] = centroids[center][2][3] + (random.random()*(centroids[rand1][2][3]-centroids[rand2][2][3]))
			else:
				rand = random.randint(0,size1-1)
				rep2[0][0][0] = centroids[rand][0][0] + (random.random()*(centroids[rand1][0][0]-centroids[rand2][0][0]))
				rep2[0][0][1] = centroids[rand][0][1] + (random.random()*(centroids[rand1][0][1]-centroids[rand2][0][1]))
				rep2[0][0][2] = centroids[rand][0][2] + (random.random()*(centroids[rand1][0][2]-centroids[rand2][0][2]))
				rep2[0][0][3] = centroids[rand][0][3] + (random.random()*(centroids[rand1][0][3]-centroids[rand2][0][3]))
				rep2[0][1][0] = centroids[rand][1][0] + (random.random()*(centroids[rand1][1][0]-centroids[rand2][1][0]))
				rep2[0][1][1] = centroids[rand][1][1] + (random.random()*(centroids[rand1][1][1]-centroids[rand2][1][1]))
				rep2[0][1][2] = centroids[rand][1][2] + (random.random()*(centroids[rand1][1][2]-centroids[rand2][1][2]))
				rep2[0][1][3] = centroids[rand][1][3] + (random.random()*(centroids[rand1][1][3]-centroids[rand2][1][3]))
				rep2[0][2][0] = centroids[rand][2][0] + (random.random()*(centroids[rand1][2][0]-centroids[rand2][2][0]))
				rep2[0][2][1] = centroids[rand][2][1] + (random.random()*(centroids[rand1][2][1]-centroids[rand2][2][1]))
				rep2[0][2][2] = centroids[rand][2][2] + (random.random()*(centroids[rand1][2][2]-centroids[rand2][2][2]))
				rep2[0][2][3] = centroids[rand][2][3] + (random.random()*(centroids[rand1][2][3]-centroids[rand2][2][3]))				



if __name__ == '__main__':
    contents = read_csv_contents('Iris.csv')
    #centroids = 
    categorise_dataset(contents)
    #print centroids