"Reinforcement Learning Gamblers Problem"
"Value iteration method to generate v* and pi*"
"@author = Prateek Bhat"

import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

py.sign_in('username', 'API key')

"Discount factor"
gamma = 1
"Probability of occurence of Head"
probhead = 0.25
"The number of states availabe"
numStates = 100
"List for storing the reward value"
reward = [0 for _ in range(101)]
reward[100]=1
"Small threshold value for comparing the difference"
theta = 0.00000001
"List to store the value function for all states form 1 to 99"
value=[0 for _ in range(101)]
"List to store the amount of bet that gives the max reward"
policy = [0 for _ in range(101)]

def gambler():
    delta = 1

    while delta > theta:
        delta = 0
        "Looping over all the states i.e the money in hand for a current episode"
        for i in range(1,numStates):
            oldvalue = value[i]
            bellmanequation(i)
            diff = abs(oldvalue-value[i])
            delta = max(delta,diff)
    print value

    # plot()
    plt.plot(policy)
    plt.show()
def bellmanequation(num):
    "Initialize optimal value to be zero"
    optimalvalue = 0

    "The range of number of bets"
    for bet in range(0,min(num,100-num)+1):
        "Amount after winning and loosing"
        win = num + bet
        loss = num - bet
        "calculate the average of possible states for an action"
        "In this case it would be Head or Tails"
        sum = probhead * (reward[win] + gamma * value[win]) + (1 - probhead) * (reward[loss] + gamma * value[loss])

        "Choose the action that gives the max reward and update the policy and value for that"
        if sum > optimalvalue:
            optimalvalue = sum
            value[num] = sum
            policy[num] = bet

"Plot the graphs for Value function and Final policy"
def plot():
    xaxis = [i for i in range(1,100)]
    del value[101:]
    del value[:1]
    del policy[101:]
    del policy[:1]
    # Create a trace

    trace = go.Scatter(
        x = xaxis,
        y = value,
        mode = 'lines'
    )

    trace1 = go.Scatter(
        x = xaxis,
        y = policy,
        mode = 'lines'
    )

    data=[trace]
    data1=[trace1]
    py.iplot(data)
    py.iplot(data1)

if __name__=="__main__":
    gambler()


