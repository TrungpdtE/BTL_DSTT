import numpy as np

A = np.random.randint(1,101,size = (10,10))
B = np.random.randint(1,21,size = (2,10))
C = np.random.randint(1,21,size = (10,2))

#a
ca=A+A.T+np.matmul(C,B)+np.matmul(B.T,C.T)
print(ca)

#b
cb=0
for k in range(1,11):
	cb=cb+(A/(9+k))**k
print(cb)

#c
cmatrix=[]
for i in range(0,A.shape[0]):
	if(i%2==0):
	  cmatrix.append(A[i,:])
vc=np.array(cmatrix)
print(vc)

#d
vd=[]
for i in range(0,A.shape[0]):
	for j in range(0,A.shape[1]):
	  if(A[i][j]%2!=0):
		vd.append(A[i][j])
newvecto=np.array(vd)
print(newvecto)

#e
ve=[]
def check_prime_numer(num):
  if num <= 1:
		return False
  for i in range(2, int(num**0.5)+1):
	 if num % i == 0:
			return False
  return True 
for i in range(0,A.shape[0]):
	for j in range(0,A.shape[1]):
	  if(check_prime_numer(A[i][j])):
		ve.append(A[i][j])
ve=np.array(ve)
print(ve)

#f
D=np.matmul(C,B)
newD=[]
for i in range(D.shape[0]):
	if(i%2==0):
	  newD=newD + [np.flipud(D[i,:])]
	else:
	  newD=newD+[D[i,:]]
newD=np.reshape(newD,(10,10))
print(newD)

#g
tempcountrow=[]
for i in range(A.shape[0]):
  count=0
  for j in range(A.shape[1]):
	if(check_prime_numer(A[i][j])):
	  count=count+1
  tempcountrow.append(count)
max=np.max(tempcountrow)
for i in range(0,len(tempcountrow)):
  if(tempcountrow[i]==max):
	print(A[i,:])

#h
count_element=[]
for i in range(A.shape[0]):
  count=0
  maxodd_row=0
  for j in range(A.shape[1]):
	if(A[i][j]%2!=0):
	  count=count+1
	else:
	  if(maxodd_row<=count):
		maxodd_row=count
	  count=0
  if(maxodd_row<=count):
	maxodd_row=count
  count_element.append(maxodd_row)
for i in range(0,len(count_element)):
  if(count_element[i]==np.max(count_element)):
	print(A[i,:])