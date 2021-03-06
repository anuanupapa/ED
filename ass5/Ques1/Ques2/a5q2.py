import numpy as np
import matplotlib.pyplot as plt
import time

#---------------
#Definitions and Variables
N_type1 = int(input('Number of TFT individual : '))
N=1000
a=3+1
b=0+1
c=5+1
d=1+1
m=4
a=m*a
b=b+(m-1)*d
c=c+(m-1)*d
d=m*d
payoff_mat = np.array([[m*a,m*b],[c*m,d*m]])/(a+b+c+d)

#---------------
#timing
ttime=time.time()
#----

#---------------
#Initialize player array
coop=np.array([[1],[0]])
defe=np.array([[0],[1]])
player_arr=[]
for i in range(N_type1):
  player_arr.append(coop)
for j in range(N-N_type1):
  player_arr.append(defe)
player_arr = np.random.permutation(player_arr)
player_index_arr=np.arange(N)
total_payoff_arr=np.zeros((N,1))
#---------------

#plotting arrays---
T=[]
frac_pop=[]
#------

#THE_GAME
def The_Game(pay_mat,parr1,parr2,M):
  temp_payoff_arr=np.zeros((N,1))
  for ind in range(len(parr1)):
    payoff1=np.dot(pay_mat[parr1[ind,1]],parr2[ind])
    payoff2=np.dot(pay_mat[parr2[ind,1]],parr1[ind])
    temp_payoff_arr[randomize[ind]]=temp_payoff_arr[randomize[ind]]+payoff1
    temp_payoff_arr[randomize[int(N/2)+ind]]=temp_payoff_arr[randomize[int(N/2)+ind]]+payoff2
  return(temp_payoff_arr/M)

#Simulation
t=0
while np.sum(player_arr[:,0])!=N and np.sum(player_arr[:,0])!=0:
  t=t+1
  #Permuting the player array
  randomize=np.random.permutation(N)
  player_arr1 = player_arr[randomize[:int(N/2)]]
  player_arr2 = player_arr[randomize[int(N/2):]]
  #PayoffGame
  payf_p_g = The_Game(payoff_mat,player_arr1,player_arr2,m)
  total_payoff_arr=total_payoff_arr+payf_p_g
  #death&birth
  birth_ind=np.random.choice(np.arange(N))
  death_ind=np.random.choice(np.arange(N))
  pay=payf_p_g[birth_ind]
  if pay<np.random.random():
    birth_ind=np.random.choice(np.arange(N))
    pay=payf_p_g[birth_ind]
  else:
    pass
  if birth_ind==death_ind:
    death_ind=np.random.choice(np.arange(N))
  else:
    pass
  if player_arr[birth_ind][0]==1:
    player_arr[death_ind]=coop
  else:
    player_arr[death_ind]=defe
  T.append(t)
  frac_pop.append(np.sum(player_arr[:,0]))
print(time.time()-ttime)
plt.plot(T,frac_pop)
plt.xlabel('Time')
plt.ylabel('Frequency of TFT')
#plt.savefig(str(N_type1)+'.png')
plt.show()
