"Value Iteration for Sports Betting"
"Value iteration helps generate v* (optimal value function) and pi* (optimal policy function)"

"Discount factor"
gamma = 1
"Probability of home team winning"
p = 0.4
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

def reinforcement_learning():
    delta = 1
    while delta > theta:
        delta = 0
        "Looping over all the states i.e the money in hand for a current episode"
        for i in range(1,numStates):
            oldvalue = value[i]
            bellmanequation(i)
            diff = abs(oldvalue-value[i])
            delta = max(delta,diff)
    print(value)

def bellmanequation(num):
    "Initialize optimal value to be zero"
    optimalvalue = 0

    "The range of number of bets"
    for bet in range(0,min(num,100-num)+1):
        "Amount after winning and losing"
        win = num + bet
        loss = num - bet
        "calculate the average of possible states for an action"
        "In this case it would be home team winning or away team winning"
        sum = p * (reward[win] + gamma * value[win]) + (1 - p) * (reward[loss] + gamma * value[loss])

        "Choose the action that gives the max reward and update the policy and value for that"
        if sum > optimalvalue:
            optimalvalue = sum
            value[num] = sum
            policy[num] = bet
            
reinforcement_learning() 
