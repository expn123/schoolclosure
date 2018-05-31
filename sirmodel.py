import numpy as np


#population number
N=1000
#number of susceptible people
S=800
#number of infectious people
I=200
#number of recovery people
#number of
#rates
transmission_rate=0.3
recovery_rate=0.2
#delta t
delta=1

n_time_steps=200


class situation:
    def __init__(self,S,I,N):
        self.number_s=S
        self.number_i=I
        self.number_r=N-self.number_s-self.number_i
        self.status = [[self.number_s,self.number_i,self.number_r]]

    def simulation(self,n):
        self.n_time_steps=n
        k=0

        while k<self.n_time_steps:
            number_infected = self.get_number_infected(self.number_s,self.number_i)
            number_recovered= self.get_number_recovered(self.number_i)
            self.number_s -= number_infected
            self.number_i  = self.number_i - number_recovered + number_infected
            self.status.append([self.number_s,self.number_i,self.get_number_r(self.number_s,self.number_i)])
            k+=1

    def get_number_infected(self,s,i):
        prob_infected = 1 - np.exp(-transmission_rate * i * delta / N)
        number_infected = np.random.binomial(s,prob_infected)
        return number_infected

    def get_number_recovered(self,i):
        prob_recovered= 1 - np.exp(-recovery_rate * delta)
        number_recovered=np.random.binomial(i,prob_recovered)
        return number_recovered

    def get_number_r(self,s,i):
        r=N-s-i
        return r



test_situation = situation (S,I,N)
test_situation.simulation(n_time_steps)
print(test_situation.status)
