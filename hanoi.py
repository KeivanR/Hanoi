import time
n = 10
first_pile = []
for i in range(n,0,-1):
	first_pile.append(i)
tab = [first_pile,[],[]]
disk = []
nothing = ''
for i in range(0,1+4*(n-1)):
	nothing+=' '
for i in range(1,n+1):
	str = ''
	for j in range(0,2*(n-i)):
		str+=' '
	for j in range(0,1+4*(i-1)):
		str+='_'
	for j in range(0,2*(n-i)):
		str+=' '
	disk.append(str)
print(disk)
def strpiece(tab_col,j):
	if j>=len(tab_col):
		return nothing
	else:
		return disk[tab_col[j]-1]
def disp(tab):
	for j in range(n-1,-1,-1):
		for i in range(0,len(tab)):
			print('|'+strpiece(tab[i],j),end='')
		print('|')
	print('')

def move(tab,n,i,j):
	if (n==1):
		tab[j].append(tab[i][-1])
		del tab[i][-1]
		disp(tab)
		time.sleep(.1)
	else:
		o = [0,1,2]
		o.remove(i)
		o.remove(j)
		k = o[0]
		move(tab,n-1,i,k)
		move(tab,1,i,j)
		move(tab,n-1,k,j)
print(tab)
move(tab,n,0,2)
