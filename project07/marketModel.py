"""
File: model.py
Author: Ken Lambert

Models multiple cashiers.
"""

from cashier import Cashier
from customer import Customer
import random

class MarketModel(object):

    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival, numCashiers):
        self._lengthOfSimulation = lengthOfSimulation
        self._averageTimePerCus = averageTimePerCus
        self._probabilityOfNewArrival = probabilityOfNewArrival
        #self._cashiers = Cashier(1)
        self._cashiers = []
        for i in range(numCashiers):
            self._cashiers.append(Cashier(i))
        
        
   
    def runSimulation(self):
        """Run the clock for n ticks."""
        for currentTime in range(self._lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self._probabilityOfNewArrival,
                currentTime,
                self._averageTimePerCus)
            
            # if successfully generated, send a customer to a cashier
            if customer != None:
#                for i in self._cashiers:
#                    #self._cashiers.addCustomer(customer)
#                    i.addCustomer(customer)
                    
                for i in self._cashiers:
                    b = 1
                    a = 0
                    right = self._cashiers[b]
                    left = self._cashiers[a]
                    
                   #left > right
                    if left.customersInLine() > right.customersInLine():
                        left = right
                        b = b + 1
                        right = self._cashiers[b]
                    #right > left
                    else :
                        b = b + 1
                        right = self._cashiers[b]
                left.addCustomer(customer) 
            


            # Tell all cashiers to provide another unit of service            
            for Cashiers in self._cashiers:
                Cashiers.serveCustomers(currentTime)
                
    def __str__(self):
        """Returns the string rep of the results of the simulation."""
        return "CASHIER CUSTOMERS   AVERAGE     LEFT IN\n" + \
               "        PROCESSED   WAIT TIME   LINE\n" + \
               "\n".join(map(str, self._cashiers))




