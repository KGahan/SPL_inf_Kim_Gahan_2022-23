sum = 0

for i in range(2,1001,2): #(initial,final but not included,gap)
  if(i%2 == 0):
    sum+= i; 

print(sum)