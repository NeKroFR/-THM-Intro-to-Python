import base64

file = open("encodedflag.txt","r")

flag = file.read()



for i in range(5):
	flag = base64.b16decode(flag)
	

for i in range(5):
	flag = base64.b32decode(flag)


for i in range(5):
	flag = base64.b64decode(flag)


print(flag)

