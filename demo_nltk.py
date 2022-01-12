import nltk
import json

input=input('Nhập một chuỗi cần sắp xếp:')

# x=input('Nhập một chuỗi cần sắp xếp:')

tokens = nltk.word_tokenize(input)

inputArray=[0,0,0,0,0,0,0,0,0,0,0]
#trọng số
# demo=[5,3,4,2,2,6,2,2,4,6,2]
demo=[4,3,2,1,3,5,1,2,5,6,4]

preInput=nltk.pos_tag(tokens,tagset="universal")
print(preInput)
# for c in preInput:
	
#đếm số nhãn có trong câu
for w in preInput:
	if w[1]=="ADJ":
		inputArray[0]+=1
		continue
	elif w[1]=='ADP':
		inputArray[1]+=1
		continue
	elif w[1]=='ADV':
		inputArray[2]+=1
		continue
	elif w[1]=='CONJ':
		inputArray[3]+=1
		continue
	elif w[1]=='DET':
		inputArray[4]+=1
		continue
	elif w[1]=='NOUN':
		inputArray[5]+=1
		continue
	elif w[1]=='NUM':
		inputArray[6]+=1
		continue
	elif w[1]=='PRT':
		inputArray[7]+=1
		continue
	elif w[1]=='PRON':
		inputArray[8]+=1
		continue
	elif w[1]=='VERB':
		inputArray[9]+=1
		continue
	else:
		inputArray[10]+=1
		continue

print(inputArray)
file=open('demo_nltk.txt','r+')
#khởi tạo 2 mảng chứa các mẫu và chữa trọng số
check=[]
similars=[]

#duyệt các mẫu có trong file
sample=file.readline()

while sample:
	
	sample=sample.split(',')

	resSample=[]

	for x in sample:
		resSample.append(int(x))

	check.append(resSample)

	#tính độ tương đồng
	res=0
	for x in range(11):
		if inputArray[x]==resSample[x]:
			res+=demo[x]
		elif (inputArray[x]==0 and resSample[x]!=0) or (inputArray[x]!=0 and resSample[x]==0):
			res+=demo[x]*0
		elif inputArray[x]>resSample[x]:
			res+=demo[x]*(resSample[x]/inputArray[x])
		else:
			res+=demo[x]*(inputArray[x]/resSample[x])

	#push độ tương đồng vào mảng
	similars.append(round(res/36,3))

	sample=file.readline()

# file.close()
i=1
vitri=1
max=0
for a in similars:
	#print("mẫu ",i,":", a)
	if a > max:
		max=a
		vitri=i
	i+=1
	
print("mẫu có độ tương đồng cao nhất là:", vitri , "độ tương đồng là:", max)

#thêm các nhãn vào mảng

with open('test1.json') as jsonfile:
	list = json.load(jsonfile)


def ABC(s, arr):
	for i in list[s[1]]['before']:
		for index, value in enumerate(arr):
			if(value[1] == i):
				arr.insert(index, s)
				return arr
	for i in list[s[1]]['after']:
		for index, value in enumerate(arr):
			if(value[1] == i):
				arr.insert(index+1, s)
				return arr

try:
	file1=open('test.txt','r')
	noidung=file1.readlines()
	print("nd: ",noidung[vitri])
	dulieu = noidung[vitri].split()
	ketqua=''
	x=[]

		# xử lý xắp xếp:
	for v in dulieu:
		for s in preInput:
			if v==s[1]:
				ketqua+=s[0]+" "
				x.append(s)
				preInput.remove(s)
				break
	line=''
	f=open('test.txt', 'a')
	# q=open('demo_nltk.txt', 'a')
	if(max != 1):
		if(len(preInput)!=0):
			for s in preInput:
				x = ABC(s,x)
			for i in range(len(x)-1): 
				line+=x[i][1]+" "
			line+=x[len(x)-1][1]+"\n"
			f.write(line)
			file.write(str(inputArray)[1:32]+"\n")

	for i in x:
		print(i[0]," ")

				
	#print(ketqua)


finally:
	f.close()
	file.close()



	