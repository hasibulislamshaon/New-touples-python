x=input("Enter the file name: ")
line=open(f'{x}','r')
dic=dict()
for lines in line:
    words=lines.split()
    for word in words:
       dic[word]=dic.get(word,0)+1
x=sorted([(v,k)for k,v in dic.items()])

print(x)