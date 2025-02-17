class Fibonacci:
 def __init__(self, count):
  self.count= count

 def sum_even_fibonacci:
  a, b = 0, 2
  total = 0
  for _ in range(self.count):
   total += b
   a,b = b, 4*b+a
  return total

fib_sum = Fibonacci(100)
print(fib_sum.sum_even_fibonacci())
