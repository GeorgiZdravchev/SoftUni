deposited_sum = float(input())
period = int(input())
interest_rate = float(input())
percent_interest_rate = interest_rate / 100
sum_rate = period * ((deposited_sum * percent_interest_rate) / 12)
sum = deposited_sum + sum_rate
print(sum)
