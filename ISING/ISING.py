

###########    Written by Fatemeh Zahed-Kachaee   ##############
###########  copyright © July-2021 all rights reserved   ##############


import numpy as np
import matplotlib.pyplot as plt
import math
from random import *



l=32
J=1
energyListInT=[]
magnetizationListInT=[]
tetaList=np.array( [0.01,0.30,0.60,0.90,1.20])
a=np.array(np.arange(1.60,3.10,0.1))
tetaList= np.append(tetaList , a)
tetaList= np.append(tetaList , [3.30,3.60,3.90,4.20])



def InitialConfiguration():
    return np.ones((l,l))

def Magnetization(mylist):
    m=0
    for i in range(l):
        for j in range(l):
            m=m+mylist[i,j] 
    return m

def ReverseSpinMagnetization(mylist,i,j):
    return 2*mylist[i,j]

def EnergyOfInitialConfiguration(mylist):
    for i in range(l):
        for j in range(l):
            e=(-J)*mylist[i][j]*(mylist[i][(j+1)%l]+mylist[(i+1)%l][j])
    return e

def ChangedSpinEnergy(myinput,i,j):
    ee=(-J)*2*(myinput[i][j])*(myinput[i][(j+1)%l]+myinput[(i+1)%l][j]+myinput[i][(j-1)%l]+myinput[(i-1)%l][j])
    return ee




for t in tetaList:
	beta= 1/t
	stepNumber=500000
	energyList=[]
	magnetizationList=[]
	configuration=InitialConfiguration()
	M=Magnetization(configuration)
	E=EnergyOfInitialConfiguration(configuration)

	for ii in range(stepNumber):
		rand=np.random.randint(0,l,2)
		rand1,rand2=rand[0],rand[1]
		configuration[rand1,rand2]= (-1)*(configuration[rand1,rand2])
		cSE=ChangedSpinEnergy(configuration,rand1,rand2)  
		rSM=ReverseSpinMagnetization(configuration,rand1,rand2)
		dltaE=E-cSE #energy of the new configuration
		if cSE<=0 or np.random.random()<= np.exp(-beta*cSE):
			E=dltaE
			M=M+(rSM) #changed_spin_list.append([rand1,rand2])
		else:
			configuration[rand1][rand2]= (-1)*(configuration[rand1][rand2])
		energyList.append(E)
		magnetizationList.append(M/(l*l))
	step=np.linspace(0,stepNumber,num=len(energyList))
	plt.figure(figsize=(15,8))
	plt.plot(step,energyList)
	plt.xlabel('Step')
	plt.ylabel('Energy')
	plt.title('Temperature'+ str(t))
	plt.grid()
	plt.savefig('ETemperature'+ str(t)+'.png')

	step=np.linspace(0,stepNumber,num=len(magnetizationList))
	plt.figure(figsize=(15,8))
	plt.plot(step,magnetizationList)
	plt.xlabel('step')
	plt.ylabel('Magnetic')
	plt.title('Temperature'+ str(t))
	plt.grid()
	plt.savefig('MTemperature'+ str(t)+'.png')

	energyListInT.append(np.array(energyList).mean())
	magnetizationListInT.append(np.array(magnetizationList).mean())
	
plt.figure(figsize=(15,8))
plt.plot(tetaList,energyListInT)
plt.xlabel('Temprture')
plt.ylabel('Energy')
plt.grid()
plt.savefig('EperT.png')

plt.figure(figsize=(15,8))
plt.plot(tetaList,magnetizationListInT)
plt.xlabel('Temprture')
plt.ylabel('Magnetization')
plt.grid()
plt.savefig('MperT.png')

