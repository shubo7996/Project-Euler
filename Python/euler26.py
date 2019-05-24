seq_length=0
for x in range(1000,1,-1):
	if seq_length>=x:
		break

	remainders=[0]*(x)
	value=1
	position=0

	while (remainders[value]==0 and value!=0):
		remainders[value]=position
		value*=10
		value%=x
		position+=1

	if (position-remainders[value]>seq_length):
		seq_length=position-remainders[value]

print(f"Result: {len(remainders)}")