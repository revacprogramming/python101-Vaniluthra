# Conditional Execution
# hrs,r=1,1
# def loop(x,y):
#   try:
#     x= float(input("Enter hours: "))
#      y= float(input("Enter rate: "))
#   except:
#     print('Enter only numerical values...')
#     loop(x,y)
#   print(x,y)
#   return x,y
  
# print(hrs,r)

# hrs,r=loop(hrs,r)
# print(hrs,r)
try:
  hrs= float(input("Enter hours: "))
  r= float(input("Enter rate: "))
except:
  print('Enter only numerical values...')
  quit()
if hrs>40:
  print('overtime!')
  t=hrs*r
  extra=(hrs-40)*.5*r
  pay=t+extra
else:
  print('regular!')
  pay=hrs*r
print('pay is:',pay)

