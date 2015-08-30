import csv
import time
from sklearn.cluster import KMeans
import numpy as np
import random
import math
import sys
sys.setrecursionlimit(100000)


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
	
    sol = []
    data = []
    for each_tuple in contents:
    	data.append(list(each_tuple[:4]))
    for i in range(0,25):
    	temp = []
    	x = random.randint(0,49)
    	temp.append(data[x])
    	x = random.randint(50,99)
    	temp.append(data[x])
    	x = random.randint(100,149)
    	temp.append(data[x])
    	sol.append(temp)
    obj = []
    for x in range(0,25):
    	print "Solution "
    	print x
    	print sol[x]
    	obj.append(compute_dist(contents,  sol[x]))
    print "Objective Functions"
    print obj
    time.sleep(5)
    centroids, obj = sorting(sol, obj, contents)
    opti_algo(centroids, obj, contents)
    #return centroid

def compute_dist(contents, centroids):
	membership = []
	for each_tuple in contents:
		tmp = []
		for a in range(0,3):
			totDst = 0
			idist = 0
			for y in range(0,4):
					idist= idist+((float(each_tuple[y])-float(centroids[a][y]))*(float(each_tuple[y])-float(centroids[a][y])))
			idist = math.sqrt(idist)
			for x in range(0,3):
				dst = 0
				for y in range(0,4):
					dst= dst+((float(each_tuple[y])-float(centroids[x][y]))*(float(each_tuple[y])-float(centroids[x][y])))
				if (dst !=0):
					totDst = totDst + ((idist/ math.sqrt(dst)) * (idist/ math.sqrt(dst)))
			if(totDst!=0):
				val = 1/totDst
			tmp.append(val)
		membership.append(tmp)
	#print membership
	#time.sleep(4)
	return obj_func(contents, centroids, membership)
		#print pos

def obj_func(contents, centroids, membership):
	tot =0
	tmp = 0
	#print membership
	for each_tuple in contents:
		for x in range(0,3):
			dist = 0
			for y in range(0,4):
				dist =  dist+ ((float(each_tuple[y])-float(centroids[x][y]))*(float(each_tuple[y])-float(centroids[x][y])))
			tot = tot + (membership[tmp][x]) * (membership[tmp][x]) * dist
		tmp= tmp + 1
	return tot

def sorting(centroids, obj, contents):
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
	print "Objective function"
	print obj
	#DBIndex(new_set[0], contents)
	return new_set, obj


def opti_algo(centroids, obj, contents):
	min_obj= obj[0]
	size1= random.randint(3, 7)
	size2= random.randint(3, 5)
	size3= random.randint(3, 5)
	size4= random.randint(3, 5)
	size5= 25 - (size1+size2+size3+size4)
	num = random.random()
	p_replace = 0.4
	p_one = 0.8
	p_one_center = 0.4
	p_two_center = 0.4
	if(num<p_replace):
		#Replacing randomly selected cluster
		print "Replacing randomly selected cluster"
		rand=  random.randint(1, 4)
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
		centroids[center][0][0]= random.uniform(float(centroids[0][0][0])-2,float(centroids[0][0][0])+0.5)
		centroids[center][0][1]= random.uniform(float(centroids[0][0][1])-2,float(centroids[0][0][1])+0.5)
		centroids[center][0][2]= random.uniform(float(centroids[0][0][2])-2,float(centroids[0][0][2])+0.5)
		centroids[center][0][3]= random.uniform(float(centroids[0][0][3])-2,float(centroids[0][0][3])+0.5)
		centroids[center][1][0]= random.uniform(float(centroids[0][1][0])-2,float(centroids[0][1][0])+0.5)
		centroids[center][1][1]= random.uniform(float(centroids[0][1][1])-2,float(centroids[0][1][1])+0.5)
		centroids[center][1][2]= random.uniform(float(centroids[0][1][2])-2,float(centroids[0][1][2])+0.5)
		centroids[center][1][3]= random.uniform(float(centroids[0][1][3])-2,float(centroids[0][1][3])+0.5)
		centroids[center][2][0]= random.uniform(float(centroids[0][2][0])-2,float(centroids[0][2][0])+0.5)
		centroids[center][2][1]= random.uniform(float(centroids[0][2][1])-2,float(centroids[0][2][1])+0.5)
		centroids[center][2][2]= random.uniform(float(centroids[0][2][2])-2,float(centroids[0][2][2])+0.5)
		centroids[center][2][3]= random.uniform(float(centroids[0][2][3])-2,float(centroids[0][2][0])+0.5)
		
		# centroids[center][0][0]= random.uniform(4,5.8)
		# centroids[center][0][1]= random.uniform(2,4.4)
		# centroids[center][0][2]= random.uniform(1,1.9)
		# centroids[center][0][3]= random.uniform(0,0.6)
		# centroids[center][1][0]= random.uniform(3.9,7)
		# centroids[center][1][1]= random.uniform(1,3.4)
		# centroids[center][1][2]= random.uniform(2,5.1)
		# centroids[center][1][3]= random.uniform(0,1.8)
		# centroids[center][2][0]= random.uniform(3.9,7.9)
		# centroids[center][2][1]= random.uniform(1.2,3.8)
		# centroids[center][2][2]= random.uniform(3.5,6.9)
		# centroids[center][2][3]= random.uniform(1,2.5)

	for x in range(0,50):
		rep2= []
		num = random.random()
		if(num<p_one):
			#Probability of generating new idea based on one cluster
			#print "Generating new idea based on one cluster"
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
				changed = center
				for a in range(0,3):
					temp = []
					for y in range(0,4):
						temp.append(float(centroids[center][a][y]) + (random.random()*(float(centroids[rand1][a][y])-float(centroids[rand2][a][y]))))
					rep2.append(temp)
			else:
				rand = random.randint(center,end)
				changed = rand
				for a in range(0,3):
					temp = []
					for y in range(0,4):
						temp.append(float(centroids[rand][a][y]) + (random.random()*(float(centroids[rand1][a][y])-float(centroids[rand2][a][y]))))
					rep2.append(temp)				
		else:
			#Generating new idea based on two cluster
			#print "Generating new idea based on two cluster"
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
				num= random.random()
				if(center1>center2):
					changed= center1
					for a in range(0,3):
						temp = []
						for y in range(0,4):
							temp.append((float(centroids[center2][a][y]))+ (num*(float(centroids[center2][a][y])-float(centroids[center1][a][y]))))
						rep2.append(temp)
				else:
					changed= center2
					for a in range(0,3):
						temp = []
						for y in range(0,4):
							temp.append((float(centroids[center1][a][y]))+ (num*(float(centroids[center1][a][y])-float(centroids[center2][a][y]))))
						rep2.append(temp)
			else:
				num= random.random()
				rand1 = random.randint(center1,end1)
				rand2 = random.randint(center2,end2)
				if(rand1>rand2):
					changed= rand1
					for a in range(0,3):
						temp = []
						for y in range(0,4):
							temp.append((float(centroids[rand2][a][y]))+ (num*(float(centroids[rand2][a][y])-float(centroids[rand1][a][y]))))
						rep2.append(temp)
				else:
					changed= rand2
					for a in range(0,3):
						temp = []
						for y in range(0,4):
							temp.append((float(centroids[rand1][a][y]))+ (num*(float(centroids[rand1][a][y])-float(centroids[rand2][a][y]))))
						rep2.append(temp)
		new_obj = compute_dist(contents, rep2)
		#print "old obj"
		#print obj[changed]
		#print "new obj"
		#print new_obj
		if(obj[changed]>new_obj):
			#print "changing"
			for r in range(0,3):
				for c in range(0,4):
					centroids[changed][r][c]= rep2[r][c]
			obj[changed]= new_obj
	new_centroid, obj = sorting(centroids, obj, contents)
	#print new_centroid
	while True:
		# print "Difference"
		# print min_obj-obj[0]
		# if((min_obj-obj[0])==0.0):
		# 	print "over"
		# 	exit()
		if(obj[0]-obj[1]==0.0):
			print "over"
			exit()
		opti_algo(new_centroid, obj, contents)

if __name__ == '__main__':
    contents = read_csv_contents('Iris.csv')
    #centroids = 
    categorise_dataset(contents)
    #print centroids

contents = read_csv_contents('Iris.csv')
global centroids
