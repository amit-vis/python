

def calculateSpan(a,n):
    span =[]
    price_ = a[::-1]
    for i in range(n):
        m=1
        for j in range(i+1, n):
            if price_[j]<price_[i]:
                m += 1
            else:
                break
        span.append(m)
    return span[::-1]


n = int(input("Enter the number of days: "))
a = list(map(int, input("Enter the stock prices: ").split()))


results = calculateSpan(a, n)
print(results)

		    

