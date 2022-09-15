line=open('touples\words.txt','r')
dic=dict()
for lines in line:
    words=lines.split()
    for word in words:
       dic[word]=dic.get(word,0)+1

dictioanry=list()
for k,v in dic.items():
    dictioanry.append((v,k))

dictioanry=sorted(dictioanry,reverse=True)
print(f"Value---Key")
for v,k in dictioanry[:5]:#number of touples that you wanted
   print(f" {v}  =  {k}")


