# recursive solution

# def max_profit_app(N, budget):
#     if N==0 or len(budget) == 0:
#         return 0
#     budget.sort()
#     current_price = budget[0]
#     eligible_subcriber = sum(b>= current_price for b in budget)
#     profit_current = eligible_subcriber*current_price

#     profit_next = max_profit_app(N-1, budget[1:])

#     return max(profit_current, profit_next)


# N = int(input("Enter the number of subscribers: "))
# budgets = list(map(int, input("Enter the budgets of subscribers (space-separated): ").split()))

# profit = max_profit_app(N, budgets)
# print("Maximum profit:", profit)

#  iterative solution

def max_profit_app_iter(arr):
    arr.sort()
    max_profit = 0
    for i in range(len(arr)-1,-1,-1):
        budget = arr[i]
        price = len(arr)-i
        subscriber = budget * price

        max_profit = max(max_profit, subscriber)

    return max_profit

n = int(input("Enter the number of subscribers: "))
budgets = list(map(int, input("Enter the budgets of subscribers (space-separated): ").split()))

ans = max_profit_app_iter(budgets)
print('max profit', ans)
