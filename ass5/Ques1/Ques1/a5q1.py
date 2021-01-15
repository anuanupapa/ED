import numpy as np
import matplotlib.pyplot as plt
import time

#---------------
#Definitions and Variables
N = int(input('Total size of population : '))
N_type1 = int(input('Number of coop individual : '))
a=3+1
b=0+1
c=5+1
d=1+1
norm=a+b+c+d
payoff_mat = np.array([[4*a,4*b],[4*c,4*d]])/(a+b+c+d+4)
m=4
#---------------
#timing
ttime=time.time()
#----

#---------------
#Initialize player array
coop=np.array([[1],[0]])
defe=np.array([[0],[1]])
#print(np.shape(coop))
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
def The_Game(pay_mat,parr1,parr2):
  temp_payoff_arr=np.zeros((N,1))
  for ind1 in range(len(parr1)):
    temp_payoff_arr[randomize[ind1]]=temp_payoff_arr[randomize[ind1]]+np.dot(pay_mat[parr1[ind1,1]],parr2[ind1])
    temp_payoff_arr[randomize[int((N/2)+ind1)]]=temp_payoff_arr[randomize[int((N/2)+ind1)]]+np.dot(pay_mat[parr2[ind1,1]],parr1[ind1])
  return(temp_payoff_arr)

#Simulation
t=0
while np.sum(player_arr[:,0])!=N and np.sum(player_arr[:,0])!=0:
  t=t+1
  #Permuting the player array
  randomize=np.random.permutation(N)
  player_arr1 = player_arr[randomize[:int(N/2)]]
  player_arr2 = player_arr[randomize[int(N/2):]]
  #PayoffGame----
  payf_p_g = The_Game(payoff_mat,player_arr1,player_arr2)
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
plt.plot(T,np.array(frac_pop)/N)
plt.xlabel('Time')
plt.ylabel('Fraction of Cooperators')
plt.savefig('a5q1.png')
plt.show()

