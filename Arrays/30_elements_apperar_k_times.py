def k_elemets(arr,n,k):
   dic={}
   x=n//k

   output=[]
   for item in arr:
       if item not in dic:
           dic[item]=1
       else:
           dic[item]+=1
   for value in dic.values():
       if value>x:
           output.append(value)
   return output

arr=[4, 5, 6, 7, 8, 4, 4]
n=len(arr)
k=3
print(k_elemets(arr,n,k))