lines=open('touples\words.txt','r')
dic=dict()
for line in lines:
    words=line.split()
    for word in words:
       dic[word]=dic.get(word,0)+1

dictioanry=list()
for k,v in dic.items():
    dictioanry.append((v,k))

dictioanry=sorted(dictioanry,reverse=True)
x=int(input("Enter the number of touples You wanted: "))
print(f"Value---Key")
y=0
for v,k in dictioanry[:x]:#number of touples that you wanted
   y=y+1
   print(f"{y}@ {v}  =  {k}")


