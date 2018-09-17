# Sports Betting with RL


## Overview

This is the code for [this](https://youtu.be/mEIePvxdbkQ) video on Youtube by Siraj Raval on Sports Betting using Reinforcement Learning. This is apart of the Move 37 course at the [School of AI](http://www.theschool.ai).

## Dependencies

None.

## Usage

Type python value_iteration.py into terminal and it will run.

## History

This is an adapted version of the "Gambler's Problem" that I've applied to sports betting. Details below

-The Gambler Problem as discussed in Example 4.3 in Reinforcement Learning: An Introduction by Richard S. Sutton and Andrew G. Barto.
-The problem from the book is described below:

**Gambler’s Problem**: A gambler has the opportunity to make bets
on the outcomes of a sequence of coin flips. If the coin comes up heads, he wins as
many dollars as he has staked on that flip; if it is tails, he loses his stake. The game
ends when the gambler wins by reaching his goal of $100, or loses by running out of
money. On each flip, the gambler must decide what portion of his capital to stake,
in integer numbers of dollars. This problem can be formulated as an undiscounted,
episodic, finite MDP. The state is the gambler’s capital, s ∈ {1, 2, . . . , 99} and the
actions are stakes, a ∈ {0, 1, . . . , min(s, 100−s)}. The reward is zero on all transitions
except those on which the gambler reaches his goal, when it is +1. The state-value
function then gives the probability of winning from each state. A policy is a mapping
from levels of capital to stakes. The optimal policy maximizes the probability of
reaching the goal. Let ph denote the probability of the coin coming up heads. If ph
is known, then the entire problem is known and it can be solved, for instance, by
value iteration
