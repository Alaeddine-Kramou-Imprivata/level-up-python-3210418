def get_prime_factors(number):
  factors = []
  divisor = 2 
  while divisor <= number:
     if number % divisor == 0:
        factors.append(divisor)
        number = number / divisor
     else:
        divisor += 1
  return factors
        
print(get_prime_factors(60))  
print(get_prime_factors(13)) 