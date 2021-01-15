import numpy as np
import matplotlib.pyplot as plt
import time

def arr_copy(arr):
  new_arr=[]
  for i in arr:
    new_arr.append(i)
  new_arr=np.asarray(new_arr)
  return(new_arr)
#---------------
#Definitions and Variables
N_type1 = 1
N_arr=[100,200,250,300,350,400,600,800,1000]
fix_prob_perN=[]
a=3
b=0
c=5
d=1
m=10
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
tft=np.array([[1],[0]])
defe=np.array([[0],[1]])
#---------------


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
for N in N_arr:
  fix_prob_counter=0
  Nt=2
  Nt=Nt*N
  #Initializing player array
  player_arr_fixed=[]
  for i in range(1):
    player_arr_fixed.append(tft)
  for j in range(N-1):
    player_arr_fixed.append(defe)
  player_arr_fixed=np.asarray(player_arr_fixed)
  player_arr_fixed = np.random.permutation(player_arr_fixed)
  #-------------------------
  for nt in range(Nt):
    t=0
    player_arr=arr_copy(player_arr_fixed)
    if nt%100==50:
      print(N, nt, fix_prob_counter)
    while np.sum(player_arr[:,0])!=N and np.sum(player_arr[:,0])!=0:
      t=t+1
      #Permuting the player array
      randomize=np.random.permutation(N)
      player_arr1 = player_arr[randomize[:int(N/2)]]
      player_arr2 = player_arr[randomize[int(N/2):]]
      #PayoffGame
      payf_p_g = The_Game(payoff_mat,player_arr1,player_arr2,m)
      #death&birth_update
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
        player_arr[death_ind]=tft
      else:
        player_arr[death_ind]=defe
    if np.sum(player_arr[:,0])==float(N):
      fix_prob_counter=fix_prob_counter+1
  fix_prob_perN.append((fix_prob_counter/Nt)*N)
  print('fix_prob '+str(fix_prob_counter/Nt))
print(time.time()-ttime)
plt.plot(N_arr, fix_prob_perN, 'ro')
x_fit=np.arange(50,1100,20)
y_fit=np.ones(np.shape(x_fit))
plt.plot(x_fit, y_fit, '.')
plt.xlabel('N (Population Size)')
plt.ylabel('Nx$\rho_{TFT}$')
plt.savefig('a6.png')
plt.show()
