prices = [7,1,5,3,6,4]
day1, day2 = 0,1
max_profit = 0
while day2 < len(prices):
    if prices[day1] < prices[day2] :
        profit = prices[day2] - prices[day1]
        max_profit = max(profit, max_profit)
    else :
        day1 = day2
    day2 += 1
print(max_profit)
