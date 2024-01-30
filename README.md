Frequent scenarios.
==================
the counter variable
--------------------
``````````````ruby
a = int(input())
b = int(input())
cnt = 0
for i in range(a, b+1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        cnt = cnt+1
print(cnt)
``````````````````````
the adder variable
------------------
`````````````````ruby
n = int(input())
total = 0
for i in range(n):
    num = int(input())
    total = total + num
print(total)
`````````````````````````
the adder and mathematics
-------------------------
````````````````````ruby
from math import *
n = int(input())
cnt = 0
for i in range(1, n+1):
    cnt = cnt+1/i
print(cnt - (log(n)))
````````````````````````
