import time
import numpy as np
import matplotlib.pyplot as plt

tim = time.time()
#----------------------
N=int(input('Number of individuals : '))
Nt=100
#----------------------

Nt_arr=[]
win_arr=[]
pop_no = N/2
for nt in range(Nt):
  #----Moran Process-----
  pop_no = N/2
  t_arr = []
  pop_arr = []
  t=0
  while pop_no!=0 and pop_no!=N:
    t=t+1
    birth = np.random.random()
    death = np.random.random()
    if birth < pop_no/N and death < pop_no/N:
      pass
    elif birth > pop_no/N and death < pop_no/N:
      pop_no = pop_no - 1
    elif birth < pop_no/N and death > pop_no/N:
      pop_no = pop_no + 1
    else:
      pass
    #print(pop_no/N)
    pop_arr.append(pop_no/N)
    t_arr.append(t)
  #plt.plot(t_arr, pop_arr)
  #plt.xlabel('time')
  #plt.ylabel('frequency of type 0')
  #plt.title('r=1')
  #plt.savefig('ques1.png')
  #plt.show()
  win_arr.append(pop_arr[-1])
  Nt_arr.append(nt)
  #---------------
print(np.sum(win_arr)/len(Nt_arr))
print(time.time()-tim)
#plt.plot(Nt_arr, win_arr, '.')
#plt.show()
