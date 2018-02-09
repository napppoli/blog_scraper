with open("wh.txt","r") as f:
	l=f.readlines()


flag=False
with open('whis.txt','a') as f:
	for i in range(len(l)):
		if '第' in l[i] and '回' in l[i]:
			flag=False
		if not flag:
			f.write(l[i])
		if '改ページ' in l[i]:
			flag=True		

