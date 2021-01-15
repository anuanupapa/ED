import time
import numpy as np
import matplotlib.pyplot as plt

tim = time.time()
#----------------------
#Initial conditions
m=10
pop_arr=[25, 50, 100,200,250,300,350,400,600,800,1000]
a=3.
b=0.
c=5.
d=1.
a=m*a
b=b+(m-1)*d
c=c+(m-1)*d
d=m*d
Nt=100
w=1. #selection strength
#----------------------

NRho_arr=[]
for pop_size in pop_arr:
  fixation_counter=0
  print(pop_size)
  for nt in range(Nt*pop_size):
    np.random.seed((nt+10)*pop_size+nt)
    pop_no = 1. # number of TFT players
    while pop_no!=0 and pop_no!=pop_size:
      birth = np.random.random()
      death = np.random.random()
      F_i = (a*(pop_no-1) +b*(pop_size-pop_no))/(pop_size-1)
      G_i = (c*pop_no+d*(pop_size-pop_no-1))/(pop_size-1)
      f_i = 1-w+w*F_i
      g_i = 1-w+w*G_i
      tot_fitness=pop_no*f_i + (pop_size - pop_no)*g_i
      TFT_fitness = pop_no*f_i/tot_fitness
      TFT_death = pop_no/pop_size
      if birth < TFT_fitness  and death < TFT_death:
        pass
      elif birth > TFT_fitness and death < TFT_death:
        pop_no = pop_no - 1
      elif birth < TFT_fitness and death > TFT_death:
        pop_no = pop_no + 1
      else:
        pass
    if int(pop_no)==pop_size:
      fixation_counter=fixation_counter+1
      print(fixation_counter)
  NRho_arr.append((fixation_counter/(Nt*pop_size))*pop_size)
print(time.time()-tim)
plt.plot(pop_arr, NRho_arr, 'o')
plt.xlabel('Population Size, N')
plt.ylabel('N$\\rho_{TFT}$')
x=np.linspace(50,1050,1100)
y=np.ones(np.shape(x))
plt.plot(x,y,',')
plt.savefig('graph_extra.png')
plt.show()
