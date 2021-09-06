# Use this file to implement your solutions
#function biggest
def biggest(lst):
	max=lst[0]
	for i in lst:
		if i>max:
			max=i
	return max

#function to find biggest two elemnent in a list

def biggest2(lst):
	max=lst[0]
	for i in lst:
		if i>max:
			max=i
	lst.remove(max)

	max2=lst[0]
	for i in lst:
		if i>max2:
			max2=i
	return [max2,max]
	
#function to find largest n numbers from a list

def biggestn(lst,m):
	res=[]
	for i in range(m):
		max=lst[0]
		for i in lst:
			if i>max:
				max=i
		res.append(max)
		lst.remove(max)
	return res[::-1]
#pangram fuction

def pangram(s):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if chat not in s.lower():
			return False
	return True

#5 fuction to return whether s in present

def ffindstring():
	import mmap
	with open(fname, 'rb', 0) as file, \
     mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as check:
    if check.find(s) != -1:
        return true

#pyton program to accept an amount 
#and count number of notes

# Function to count and print 
# currency notes
def countCurrency(amount):
	notes = [2000,500,200,100,50,20,10,5,1]
	noteCounter = [0,0,0,0,0,0,0,0,0]
	print ("currency count -> ")
	for i,j in zip(notes, noteCounter):
		if amount >=i:
			j = amount // i
			amount =amount - j * i
			dic={}
			dic[i]=j
			print(dic)

