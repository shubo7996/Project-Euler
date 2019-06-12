import time

start=time.perf_counter()

odd=['1','3','5','7','9']

def check(n):
	count_=0
	for each in str(n):
		if each in odd:
			count_+=1
	if count_==len(str(n)):
		return True

count=0
repeat=[]
for x in range(1,int(1E9)):
	if str(x)[-1::-1][0]=='0':
		continue
	elif x in repeat or int(str(x)[-1::-1]) in repeat:
		count+=1
	else:
		sum_=x+int(str(x)[-1::-1])
		fn=check(sum_)
		if fn:
			count+=1
			repeat.extend([x,int(str(x)[-1::-1])])
print(count)		
print(f"Time Elapsed: {time.perf_counter()-start}")