import numpy as np
import matplotlib.pyplot as plt
import time
from scipy import stats

#-----
#Definitions and Variables
Nt=100
#perc = float(input('Fraction of A players : '))
#u1 = float(input('Mutation rate of A to B = '))
#u2 = float(input('Mutation rate of B to A = '))
perc=0.5
u1=0.003
u2=0.001
ti=time.time()
T = 2500
#-----
N_arr=[50,100,200,300,400,600,800,1000,5000]
mean_arr=[]
var_arr=[]
N_inv=[]

def lin_fit(X,m,c):
  ret_arr=[]
  for x in X:
    ret_arr.append(m*x+c)
  np.asarray(ret_arr)
  return(ret_arr)

for N in N_arr:
  freq=[]
  freq_squared=[]
  for iter in range(Nt):
    Time=[]
    freq_A_evol_arr=[]
    
    frac_A=int(N*perc)
    frac_A_temp=frac_A
    for i in range(T):
      for a in range(int(frac_A)):
        if np.random.random()<u1:
          frac_A_temp=frac_A_temp-1
        else:
          pass
      for b in range(int(N-frac_A)):
        if np.random.random()<u2:
          frac_A_temp=frac_A_temp+1
        else:
          pass
      frac_A=frac_A_temp
      freq_A_evol_arr.append(frac_A/N)
      Time.append(i)
    freq.append(frac_A/N)
    freq_squared.append((frac_A/N)**2)
    if iter==Nt-1:
      plt.plot(Time,freq_A_evol_arr,'.')
      plt.xlabel('Time unit')
      plt.ylabel('Frequency of A')
      plt.title('Population Size'+str(N))
      plt.savefig('PopsizeN'+str(N)+'.png')
      #plt.show()
      plt.clf()
  Mean=np.sum(freq)/len(freq)
  mean_arr.append(Mean)
  var_arr.append((np.sum(freq_squared)/len(freq)) - (Mean)**2)
  N_inv.append(1/N)

plt.plot(N_arr,mean_arr,'.')
plt.show()
plt.clf()
plt.plot(N_inv,var_arr,'.')
plt.xlabel('1/N')
plt.ylabel('Variance')
s,t,p,q,std_err = stats.linregress(N_inv,var_arr)
Test_arr = lin_fit(N_inv,s,t)
plt.plot(N_inv,Test_arr)
plt.savefig('N_invVSvar'+str(T)+'.png')
plt.show()
print(time.time() - ti)
