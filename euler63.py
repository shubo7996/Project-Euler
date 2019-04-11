#euler63

counter=0
for x in range(1,10):
  power=1
  while True:
    if power==len(str(x**power)):
      counter+=1
    else:
      break
    power+=1

print(counter)
