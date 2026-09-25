# Bank-Counter
This project was done for a (beginners') Python university course. It was written with Python and file-handling in Python.

The main objective of this project is to distribute n number of customers between three bank counters according to 2 metrics:
1. How long their business is expected to take
2. How many customers are already in each counter

Two inputs must be entered for each customer: 
1. Time entered
2. Expected time
Customers are first placed on empty counters, if available. If not, they are placed on the counter with the least number of customers AND wait time.

The output displays when key events such as a customer walking up to a counter, and leaving, takes place. The time is displayed in numbers, which can be both interpreted as minutes or seconds, although the conversion of numbers greater than 60 does not happen. (That is by design)

Moreover, more statistics will be printed after all customers have left such as:
1. The average of difference between expected time and the actual time spent in the bank
2. The Average of Expected time in the bank
3. The Average of time spent in the bank for customers

# How would I build on this idea?
1. A more complex optimization algorithm to minimize the average time spent could be implemented, instead of a First Come First Serve basis.
2. Adding Graphics to simulate customers entering and leaving in real-time for better readability. The output is currently only text-based, which makes it hard to follow as the number of customers increase.

# How to run this code:
There's only one Python file. Simply copy the wall of text and put it in a compiler of your liking. Then run. 
