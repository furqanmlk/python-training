# Function will find max profit but, will fail when stocks value are desending order
def max_profit(stock_prices):

    '''
    stocks = [23,12,3,10]
    price =                                         23, 12, 3, 10
    min_price =                                     23, 12, 3, 3 
    currentProfit = price - min_price ->            0, 0, 0 , 7
    max_profit = max(currentProfit, max_profit) ->  0, 0, 0 , 7
    '''

    # Edge case, if there is less than 2 element, raise exception
    if len(stock_prices) < 2:
        raise Exception("Need at least two stocks prices !")
    
    # set minumum price marker
    min_price = stock_prices[0]
    max_profit = 0

    for price in stock_prices:

        # find the min stock price so far
        if (price < min_price):
            min_price = price
        
        # current profit so far
        currentProfit = price - min_price

        if (currentProfit > max_profit):
            max_profit = currentProfit
    
    return max_profit
        

def max_profit_02(stock_prices):

    '''
    intput = [30,22,21,5]
    price  =       30, 22, 21
    min_price =    30, 22, 21
    currentProfit = price - min_price -> 0,0
    max_profite =  -8 (22-30) -> -8, 0,,0

    '''
    # checking length
    if len(stock_prices) < 2 :
        raise Exception("Need at least two stock pricess !")
    
    # Set minimum pricess marker
    min_price = stock_prices[0]

    # Set max profit
    max_profit = stock_prices[1]-stock_prices[0]
    
    # skip first index of 0
    for price in stock_prices[1:]:

        # Note the reordering (see above function) here due to the negative profit tracking

        # Checking current profit first
        currentProfit = price - min_price

        # Finding max profit
        if currentProfit > max_profit:
            max_profit = currentProfit
      
        # Finding min prices so far
        if min_price > price:
            min_price = price
    
    return max_profit


# stocks = [23,12,3,10]
# print(max_profit(stocks))

intput = [30,22,21,5]
print(max_profit_02(intput))