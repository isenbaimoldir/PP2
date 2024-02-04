''' 
    rabbit = (numlegs - 2numheads) /2
    chicken = numheads - rabbit
'''

def solve(numheads, numlegs):
    rabbit = (numlegs - 2 * numheads)/2
    chicken = numheads - rabbit
    return f"The number of rabbit is {rabbit}, and the number of chiken is {chicken}"

head = int(input())
leg = int(input())
print(solve(head, leg))