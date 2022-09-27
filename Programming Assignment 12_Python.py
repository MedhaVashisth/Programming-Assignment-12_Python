#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()

# initializing dictionary
test_dict = {'gfg' : [5, 6, 7, 8],
			'is' : [10, 11, 7, 5],
			'best' : [6, 12, 10, 8],
			'for' : [1, 2, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()
res = list(sorted({ele for val in test_dict.values() for ele in val}))

# printing result
print("The unique values list is : " + str(res))


# In[2]:


# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))


# In[3]:


dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)


# In[4]:


# Python3 code to demonstrate working of
# Convert key-values list to flat dictionary
# Using dict() + zip()
from itertools import product

# initializing dictionary
test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
# Using dict() + zip()
res = dict(zip(test_dict['month'], test_dict['name']))

# printing result
print("Flattened dictionary : " + str(res))


# In[5]:


# Python3 code to demonstrate working of
# Convert key-values list to flat dictionary
# initializing dictionary
test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
x=list(test_dict.values())
a=x[0]
b=x[1]
d=dict()
for i in range(0,len(a)):
	d[a[i]]=b[i]
# printing result
print("Flattened dictionary : " + str(d))


# In[6]:


# Python code to demonstrate
# insertion of items in beginning of ordered dict
from collections import OrderedDict

# initialising ordered_dict
iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])

# inserting items in starting of dict
iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last = False)

# print result
print ("Resultant Dictionary : "+str(iniordered_dict))


# In[7]:


# Function to check if string follows order of
# characters defined by a pattern
from collections import OrderedDict

def checkOrder(input, pattern):
	
	# create empty OrderedDict
	# output will be like {'a': None,'b': None, 'c': None}
	dict = OrderedDict.fromkeys(input)

	# traverse generated OrderedDict parallel with
	# pattern string to check if order of characters
	# are same or not
	ptrlen = 0
	for key,value in dict.items():
		if (key == pattern[ptrlen]):
			ptrlen = ptrlen + 1
		
		# check if we have traverse complete
		# pattern string
		if (ptrlen == (len(pattern))):
			return 'true'

	# if we come out from for loop that means
	# order was mismatched
	return 'false'

# Driver program
if __name__ == "__main__":
	input = 'engineers rock'
	pattern = 'er'
	print (checkOrder(input,pattern))


# In[8]:


# Function calling
def dictionairy():
	# Declare hash function
	key_value = {}

# Initializing value
	key_value[2] = 56
	key_value[1] = 2
	key_value[5] = 12
	key_value[4] = 24
	key_value[6] = 18
	key_value[3] = 323

	print("Task 1:-\n")

	print("key_value", key_value)

	# iterkeys() returns an iterator over the
	# dictionary’s keys.
	for i in sorted(key_value.keys()):
		print(i, end=" ")


def main():
	# function calling
	dictionairy()


# Main function calling
if __name__ == "__main__":
	main()


# In[ ]:




