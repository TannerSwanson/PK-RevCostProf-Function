import matplotlib.pyplot as plt
'''Currently models and graphs the revenue, cost, profit, and a possible referal payout for the bulk ordering of a product.
Initially models 0-50 customers, and supports discounts related to size, referals, and free items. 
The referal system comes from a question on the original google form and currently has to be manually inputted into the referalList list,
but I am currently working to implement a google API to automate this process and make the referal # more accurate.
'''
def discountModel(price, users): #models discounts from vendor. Standard bulk order from vendor
    if (users >= 10): #discounts are unique to vendor
        bulkDiscount = .625
    elif (users >= 5):
        bulkDiscount = .875
    else:
        bulkDiscount = 1
    if (users >= 30): #Additional discount code due to relationship with vendor
        discountCode = .5
    else:
        discountCode = .75
    return price * bulkDiscount * discountCode

def costModel(users, myRate, FreeItems):
    price = discountModel(5, users) #generates price given potential discounts from vendor
    VendorCharge = (users * price)
    ourCollection = (users * myRate)
    profit = ourCollection - VendorCharge - (FreeItems * myRate) #accounts for any free items given out
    return profit

def createProfit(myRate, FreeItems=0): #creates a list of profit for 0-99 customers
    returnList = []
    for i in range(0, 50):  #models total profit for 99 customers
        profit = costModel(i, myRate, FreeItems)
        returnList.append(profit)
    return returnList


def referal(referalList, findersFee): #function models potential referal program for items
    total = []
    cummulative = 0
    for i in range(len(referalList)): #adds up total number of referals. Assumes first n purchases are referals for a total of n referals
        cummulative += referalList[i][1] #referalList[i][1] is the # of referals per person
    for j in range(0, 50): #simulates for 100 people 
        if j < cummulative:
            total.append(j * findersFee)
        else:
            total.append(cummulative * findersFee)
    return total

referalList = [["mari", 6], ["emma", 6], ["ian", 9]] #sample data. data can be found from google sheet column E. Plans to implement google sheets API
StandardRate = createProfit(4, 3) #rate ($), FreeItems #
referalPay = referal(referalList, 2.5) #referalList, findersFee ($)

#models revenue and how much vendor is charging 
cost = []
for i in range(0, 50):
    func = discountModel(5, i) * i
    cost.append(func)
revenue = []
for i in range(0, 50):
    total = i * 5 #number of people * rate to find total revenue
    revenue.append(total)

#Plotting for standard rate, cost from vendor, revenue, and potential referal payouts
plt.plot(StandardRate, color='green', marker='o', label='profit')
plt.plot(referalPay, color='red', marker='o', label='referal payout')
plt.plot(cost, color='gray', marker='o', label='cost')
plt.plot(revenue, color='black', marker='o', label='revenue')
plt.legend(loc="upper left")

plt.xticks(range(0, len(StandardRate)+1, 5))
plt.ylabel('$')
plt.xlabel('People Ordering')
plt.title("People to $ graph")
plt.show()