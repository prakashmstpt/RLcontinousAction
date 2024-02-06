import numpy as np
import matplotlib.pyplot as plt
def genRndDemand52wk():
	np.random.seed(0)
	demand_hist = []
	for i in range(52):
    		for j in range(4):   #Mon - Thu 3 unit with SD 1.5
        		random_demand = np.random.normal(3, 1.5)
        		if random_demand < 0:
            			random_demand = 0
        		random_demand = np.round(random_demand)
        		demand_hist.append(random_demand)
    		random_demand = np.random.normal(6, 1) 	#Fri 6 unist with SD 1
    		if random_demand < 0:
        		random_demand = 0
    		random_demand = np.round(random_demand)
    		demand_hist.append(random_demand)
    		for j in range(2):  #Weekend demand 12 with SD 2
        		random_demand = np.random.normal(12, 2)
        		if random_demand < 0:
            			random_demand = 0
        		random_demand = np.round(random_demand)
        		demand_hist.append(random_demand)
	return demand_hist
