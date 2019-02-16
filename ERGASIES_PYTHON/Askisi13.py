def loop(ulist,limit,max_now,arxi,telos):  
   for i in range(telos,arxi,-1):
      if((ulist[i]+max_now)<=limit):
         max_now+=ulist[i]
         loop(ulist,limit,max_now,arxi,i-1)
   return(max_now)

def maxDistance(ulist,limit):
   ulist.sort()
   max_final=0
   max_now=0

   if(sum(ulist)<limit):
      return sum(ulist)

   for arxi in range(len(ulist)):
      max_now=ulist[arxi]
      for telos in range(len(ulist)-1,arxi,-1):
         if((ulist[telos]+max_now)<=limit):      
            max_now=loop(ulist,limit,max_now,arxi,telos)
            max_final=max(max_now,max_final)

   return max_final



list_user=input("Please insert a list of numbers: ")
list_user=(list_user.split())
for i in range(len(list_user)):
      list_user[i]=int(list_user[i])
max_user=int(input("Please insert a limit: "))

print("The maximum sum is: ",maxDistance(list_user,max_user))