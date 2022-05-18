largest =0
smallest =50
while True:
  num = input("Enter a number: ")
  try:
    num1=int(num)
  except:
    if num == "done":
      break
    else:
      print('Invalid input')
  if num1>largest:
    largest=num1
  if num1<smallest:
    smallest=num1

print("Maximum is", largest)
print("Minimum is",smallest)