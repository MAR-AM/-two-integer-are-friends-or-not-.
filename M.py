nbr1=int(input('Enter the first number : '))
nbr2=int(input('Enter the second number : '))
sum1=0
sum2=0
for divider in range (2,nbr1):
  if nbr1 % divider==0:
    sum1=sum1+divider
for divider in range (2,nbr2):
  if nbr2 % divider==0:
    sum2=sum2+divider

if sum2==nbr1 and sum1==nbr2 :
  print('the two integers are friends.')
else:
  print('the two integers are not friends !')