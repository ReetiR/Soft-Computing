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
	
    class1 = []
    class2 = []
    class3 = []
    for each_tuple in contents:
        if each_tuple[0] == '1':
            class1.append(list(each_tuple[1:]))
            #iris_virginica = list(iris_virginica)
        elif each_tuple[0] == '2':
            class2.append(list(each_tuple[1:]))
            #iris_versicolor = list(iris_versicolor)
        elif each_tuple[0] == '3':
            class3.append(list(each_tuple[1:]))
            #iris_setosa = list(iris_setosa)
    sol = []

    for i in range(0,25):
    	temp = []
    	x = random.randint(0,58)
    	temp.append(class1[x])
    	x = random.randint(0,70)
    	temp.append(class2[x])
    	x = random.randint(0,47)
    	temp.append(class3[x])
    	sol.append(temp)
    obj = []
    for x in range(0,25):
    	print "Solution "
    	print x
    	print sol[x]
    	obj.append(compute_dist(contents,  sol[x]))
    print "Objective Functions:"
    #print obj
    centroid, obj = cluster(sol, obj)
    print "Step before optimization"
    opti_algo(centroid, obj, contents)
    #return centroid

def compute_dist(contents, centroids):
	membership = []
	for each_tuple in contents:
		min_dist = 10000
		dst = 0
		for x in range(0,3):
			for y in range(0,13):
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
		for x in range(0,13):
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
		new_set.append(centroids[pos])
	obj.sort()
	print obj
	return new_set, obj

def opti_algo(centroids, obj, contents):
	min_obj= obj[0]
	size1= random.randint(2, 7)
	size2= random.randint(2, 7)
	size3= random.randint(2, 7)
	size4= random.randint(2, 7)
	size5= 25 - (size1+size2+size3+size4)
	print size1
	print size2
	print size3
	print size4
	print size5
	num = random.random()
	p_replace = 0.2
	p_one = 0.8
	p_one_center = 0.4
	p_two_center = 0.5
	if(num<p_replace):
		#Replacing randomly selected cluster
		print "Replacing randomly selected cluster"
		rand=  random.randint(0, 4)
		if (rand==0):
			center = 0
		elif (rand==1):
			center = size1
		elif (rand==2):
			center = size1+size2
		elif (rand==3):
			center = size1+size2+size3
		else:
			center = size1+size2+size3+size4
		centroids[center][0][0]= random.uniform(12.85,14.83)
		centroids[center][0][1]= random.uniform(1.35,4.04)
		centroids[center][0][2]= random.uniform(2.04,3.22)
		centroids[center][0][3]= random.uniform(11.2,25)
		centroids[center][0][4]= random.uniform(89,132)
		centroids[center][0][5]= random.uniform(2.2,3.88)
		centroids[center][0][6]= random.uniform(2.19,3.93)
		centroids[center][0][7]= random.uniform(0.17,0.5)
		centroids[center][0][8]= random.uniform(1.25,2.96)
		centroids[center][0][9]= random.uniform(3.52,8.9)
		centroids[center][0][10]= random.uniform(0.82,1.28)
		centroids[center][0][11]= random.uniform(2.51,4)
		centroids[center][0][12]= random.uniform(680,1680)

		centroids[center][1][0]= random.uniform(11.03,13.86)
		centroids[center][1][1]= random.uniform(0.74,5.8)
		centroids[center][1][2]= random.uniform(1.36,3.23)
		centroids[center][1][3]= random.uniform(10.6,30)
		centroids[center][1][4]= random.uniform(70,162)
		centroids[center][1][5]= random.uniform(1.1,3.52)
		centroids[center][1][6]= random.uniform(0.57,5.08)
		centroids[center][1][7]= random.uniform(0.13,0.66)
		centroids[center][1][8]= random.uniform(0.41,3.58)
		centroids[center][1][9]= random.uniform(1.28,6)
		centroids[center][1][10]= random.uniform(0.69,1.71)
		centroids[center][1][11]= random.uniform(1.59,3.69)
		centroids[center][1][12]= random.uniform(278,985)

		centroids[center][2][0]= random.uniform(12.2,14.34)
		centroids[center][2][1]= random.uniform(1.24,5.65)
		centroids[center][2][2]= random.uniform(2.1,2.86)
		centroids[center][2][3]= random.uniform(17.5,27)
		centroids[center][2][4]= random.uniform(80,123)
		centroids[center][2][5]= random.uniform(0.98,2.8)
		centroids[center][2][6]= random.uniform(0.34,1.57)
		centroids[center][2][7]= random.uniform(0.17,0.63)
		centroids[center][2][8]= random.uniform(0.55,2.7)
		centroids[center][2][9]= random.uniform(3.85,13)
		centroids[center][2][10]= random.uniform(0.48,0.96)
		centroids[center][2][11]= random.uniform(1.27,2.47)
		centroids[center][2][12]= random.uniform(415,880)
		
	for x in range(0,25):
		rep2= []
		num = random.random()
		if(num<p_one):
			#Probability of generating new idea based on one cluster
			print "Probability of generating new idea based on one cluster"
			num =  random.random()
			if (size1>size2) and (size1>size3) and (size1>size4) and (size1>size4) and (size1>size5):
				center = 0
				rand1 = random.randint(0,size1-1)
				rand2= random.randint(0,size1-1)
				end = size1-1
			elif (size2>size3) and (size2>size4) and (size2>size5):
				center = size1
				rand1 = random.randint(size1,size1+size2-1)
				rand2= random.randint(size1,size1+size2-1)
				end = size1+size2-1
			elif (size3> size4) and (size3>size5):
				center = size1+size2
				rand1 = random.randint(size1+size2, size1+size2+size3-1)
				rand2= random.randint(size1+size2, size1+size2+size3-1)
				end = size1+size2+size3-1
			elif (size4>size5):
				center = size1+size2+size3
				rand1 = random.randint(size1+size2+size3, size1+size2+size3+size4-1)
				rand2= random.randint(size1+size2+size3, size1+size2+size3+size4-1)
				end = size1+size2+size3+size4-1
			else:
				center = size1+size2+size3+size4
				rand1 = random.randint(size1+size2+size3+size4, 24)
				rand2= random.randint(size1+size2+size3+size4, 24)
				end= 24
			if(num<p_one_center):
				#Probability of using cluster center
				print "Probability of using cluster center"
				changed = center
				for a in range(0,3):
					temp = []
					for y in range(0,13):
						temp.append(float(centroids[center][a][y]) + (random.random()*(float(centroids[rand1][a][y])-float(centroids[rand2][a][y]))))
					rep2.append(temp)
			else:
				rand = random.randint(center,end)
				changed = rand
				for a in range(0,3):
					temp = []
					for y in range(0,13):
						temp.append(float(centroids[rand][a][y]) + (random.random()*(float(centroids[rand1][a][y])-float(centroids[rand2][a][y]))))
					rep2.append(temp)				
		else:
			#Generating new idea based on two cluster
			print "Generating new idea based on two cluster"
			randj1= random.randint(0,4)
			randj2= random.randint(0,4)
			while(randj1==randj2):
				randj2= random.randint(0,4)
			if (randj1==0):
				center1 = 0
				end1 = size1-1
			elif (randj1==1):
				center1 = size1
				end1 = size1+size2-1
			elif (randj1==2):
				center1 = size1+size2
				end1 = size1+size2+size3-1
			elif (randj1==3):
				center1 = size1+size2+size3
				end1 = size1+size2+size3+size4-1
			else:
				center1 = size1+size2+size3+size4
				end1= 24
			if (randj2==0):
				center2 = 0
				end2 = size1-1
			elif (randj2==1):
				center2 = size1
				end2 = size1+size2-1
			elif (randj2==2):
				center2 = size1+size2
				end2 = size1+size2+size3-1
			elif (randj2==3):
				center2 = size1+size2+size3
				end2 = size1+size2+size3+size4-1
			else:
				center2 = size1+size2+size3+size4
				end2= 24
			num= random.random()
			if(num<p_two_center):
				#Probability of using cluster center
				print "Probability of using cluster center"
				changed = center1
				for a in range(0,3):
					temp = []
					for y in range(0,13):
						temp.append((num*float(centroids[center1][a][y]))+ ((1-num)*float(centroids[center2][a][y])))
					rep2.append(temp)
			else:
				rand1 = random.randint(center1,end1)
				rand2 = random.randint(center2,end2)
				changed = rand1
				for a in range(0,3):
					temp = []
					for y in range(0,13):
						temp.append((num*float(centroids[rand1][a][y])) + ((1-num)*float(centroids[rand2][a][y])))
					rep2.append(temp)
		new_obj = compute_dist(contents, rep2)
		print "old obj"
		print obj[changed]
		print "new obj"
		print new_obj
		if(obj[changed]>new_obj):
			print "changing"
			print obj[changed]
			print "to"
			print new_obj
			for x in range(0,3):
				for y in range(0,13):
					centroids[changed][x][y]= rep2[x][y]
			obj[changed]= new_obj
		else:
			print "No need for change"
		centroids, obj = cluster(centroids, obj)
	new_centroid, obj = cluster(centroids, obj)
	#print new_centroid
	while True:
		print "Difference"
		print min_obj-obj[0]
		if((min_obj-obj[0])==0.0):
			print "over"
			exit()
		opti_algo(new_centroid, obj, contents)

if __name__ == '__main__':
    contents = read_csv_contents('wineData.csv')
    #centroids = 
    categorise_dataset(contents)
    #print centroids