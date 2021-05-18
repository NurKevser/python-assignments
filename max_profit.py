

```
Given an array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. Note that you must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

Example of different list of stock prices and respective outputs.

List = [75,73,60,100,120,130]
Output = 70
List = [10,20,23,22,17,30]
Output = 20
List = [1,6,19,59,30,60]
Output = 59
```

def stock_max_profit(liste):
  #liste = [10,20,23,22,17,30]
  buy = min(liste)
  sell = max(liste[liste.index(buy)::])
  max_profit= sell - buy
  return max_profit
stock_max_profit([130,73,60,100,120,75])  
