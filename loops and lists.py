#Q1:DEBUG BELOW CODE
# def has_lucky_number(nums):
#     """Return whether the given list of numbers is lucky. A lucky list contains
#     at least one number divisible by 7.
#     """
#     for num in nums:
#         if num % 7 == 0:
#             return True
#         else:
#             return False

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    
    return False

#Q2
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    res=[]
    for i in range(0,len(L)):
        if L[i]>thresh:
            res.append(True)
        else:
            res.append(False)
    
    return res

#Q3
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(1,len(meals)):
        if(meals[i]==meals[i-1]):
            return True
        
    return False

#Q4Next to the Blackjack table, the Python Challenge Casino has a slot machine. You can get a result from the slot machine by calling play_slot_machine(). The number it returns is your winnings in dollars. Usually it returns 0. But sometimes you'll get lucky and get a big payday. Try running it below:
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    avg_payout = sum(payouts) / n_runs
    return avg_payout

def play_slot_machine():
    pass