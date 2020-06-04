import re 

def give_vars2(ster):
	mb = re.findall('message@([^@]+)',ster)
	#if mb[0]==None : mb[0]='hello'
	mal = re.findall('to ([^ ]+)',ster)
	try : 
		mal.append(mb[0])
	except :
		mb = re.findall('msg@([^@]+)',ster)
		try : 
			mal.append(mb[0])

		except :
			mal.append('hello')
	finally : return mal


print(give_vars2('msg@hello@ to rahulmala18@gmail.com'))