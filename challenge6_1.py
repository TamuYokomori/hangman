# call another function of built-in module; statisticsa

import statistics

a = [1, 2, 3, 4, 4]
result1 = statistics.mean(a)
print(result1)

result2 = statistics.fmean(a)
print(result2)

b = [54, 24, 36]

result3 = round(statistics.geometric_mean(b), 1)
print(result3)


# call the function of challenge6-2 by importing

import challenge6_2

result = challenge6_2.challenge6_2(987)
print(result)

