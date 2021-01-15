import numpy as np
import matplotlib.pyplot as plt
import time

#---------------
#Definitions and Variables
N = int(input('Total size of population : '))
type0fixed = int(input('Number of type 0 individual : '))
u0 = float(input('Mutation rate of 0 to 1 = '))
u1 = float(input('Mutation rate of 1 to 0 = '))
f0 = float(input('Fitness of type 0 : '))
f1 = float(input('Fitness of type 1 : '))
Nt = int(input('Number of trials : '))
#---------------
#timing
ttime=time.time()
#----

fixation_prob_type0 = 0
fixation_prob_type1 = 0

for i in range(Nt):
  type0 = type0fixed
  type0_frac_arr = []
  Time = []
  t=0
  #for bb in range(N*1000):
  while type0 != 0 and type0 != N:
    #-------------------------
    #initialization of random numbers before every iteration
    t=t+1
    type0_temp = type0
    randmut0 = np.random.random()
    randmut1 = np.random.random()
    randselbirth = np.random.random()
    randseldeath = np.random.random()
    mutation_selector = np.random.random()
    pop_rat = type0/N
    death_cutoff = type0/N
    birth_cutoff = (f0*type0)/(f0*type0 + f1*(N-type0))
    tot_fitness = (f0*type0 + f1*(N-type0))

    #--------------------
    #loop for determining selection
    if randselbirth < birth_cutoff and randseldeath < death_cutoff:
      pass
    elif randselbirth > birth_cutoff and randseldeath < death_cutoff:
      type0_temp = type0_temp - 1
    elif randselbirth < birth_cutoff and randseldeath > death_cutoff:
      type0_temp = type0_temp + 1
    else:
      pass
    
    #---------------------
    #loop for determining mutation
    if mutation_selector < pop_rat:
      if randmut0 < u0:
        type0_temp = type0_temp-1
      else:
        pass
    else:
      if randmut1 < u1:
        type0_temp = type0_temp+1
      else:
        pass
    #----------------------
    type0 = type0_temp
    type0_frac_arr.append(type0/N)
    Time.append(t)
  '''
  plt.plot(Time,type0_frac_arr)
  plt.xlabel('Time')
  plt.ylabel('Frequency of type 0')
  plt.title('u0='+str(u0)+' u1='+str(u1)+' f0='+str(f0)+' f1='+str(f1)+' Final population ratio:'+str(pop_rat))
  plt.savefig('N'+str(N)+'u0'+str(u0)+'u1='+str(u1)+'f0='+str(f0)+'f1'+str(f1)+'.png')
  plt.show()
  '''
  fixation_prob_type0 = fixation_prob_type0 + type0_frac_arr[-1]
  fixation_prob_type1 = fixation_prob_type1 + (1-type0_frac_arr[-1])
print('type0 : '+str(fixation_prob_type0/Nt))
print('type1 : '+str(fixation_prob_type1/Nt))
print(time.time() - ttime)

#Calculting the theoretical value for equilibrium frequeny in presence of mutation
if u0!=0 or u1!=0:
  sq_rt = np.sqrt((f0-f1-u0-u1)**2 - 4*(f1-f0)*u1)
  term1_num = (u0+u1+f1-f0)
  print(max((term1_num+sq_rt)/(2*(f1-f0)), (term1_num-sq_rt)/(2*(f1-f0))))

#Calculating the theoretical value for fixation probability
if u0==0 and u1==0:
  numerator = 1-(1/(f1**1))
  denominator = 1-(1/(f1**N))
  print(numerator/denominator)
