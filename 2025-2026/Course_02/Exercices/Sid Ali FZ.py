#####################################################################@@@
# Solution 1:  Display numbers from a list using a loop &&&&&&&
numbers=[12, 75, 150, 180, 145, 525, 50]
for n in  numbers :
 if n%5==0:
  if n<=150 :
    print(n)
    continue
  if n>500 :
   break
 """ 
################################################################################
#Solution 2: Display Fibonacci series up to terms  &&&&&
  
N=int(input("inter the numbers of terms of Fibonacci series :"))

Fibon_s1=0
Fibon_s2=1
print(Fibon_s1)
print(Fibon_s2)
i=1
while i < N-1 :
 Fibon_s=Fibon_s1+Fibon_s2
 print(Fibon_s)
 Fibon_s1=Fibon_s2
 Fibon_s2=Fibon_s
 i+=1


#####################################################################@@@
# Solution 4 &&&&&& Find the factorial of a given number N &&&&&&&
N=int(input("inter the value of N:"))
N_fac=1
for i in range(1,N+1):
 N_fac=N_fac* i
print("N!=", N_fac)
#############################################################################
# Solution 4 &&&&&& Find the factorial of a given number &&&&&&& second method
N=int(input("inter the value of N:"))
N_fac=1
i=1
while i<=N:
 N_fac=N_fac* i
 i+=1
print("N!=", N_fac)

 
 """