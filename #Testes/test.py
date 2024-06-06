import re
#print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])

# ^\([0-9]{2}\)\s9[0-9]{4}[-][0-9]{4}$

pattern = r'^\([0-9]{2}\)\s9[0-9]{4}[-][0-9]{4}$'
tel = '(21) 98888-8888'
result = re.search(pattern, tel) 

if result:
  print(True)
else:
  print(False)




