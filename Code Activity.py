import random

# Task 1
def get_sum_even_numbers_while(n):
        sum_even = 0 
        i = 0
        while i <= n:
                if i % 2 == 0:
                        sum_even += i 
                i += 1
        return sum_even

def get_sum_even_numbers_for(n):
        sum_even = 0
        for i in range(1, n+1):
                if i % 2 == 0:
                      sum_even += i
        return sum_even

# Task 2
def random_generator(n):
        return[random.randint(1, 1000) for _ in range(n)]

# Task 3
def random_generator_unique(n):
        random_numbers = set()
        while len(random_numbers) < n:
                random_numbers.add(random.randint(1, 1000))
        return list(random_numbers)

# Task 4 
def get_random_numbers(n, x):
        if x > n:
                raise ValueError(" X Should Be Less Than Or Equal To N")
        all_numbers = random_generator_unique(n)
        return
        random.sample(all_numbers,x)

# EXAMPLE USAGE
if __name__=="__main__":
        n = 10
        x = 5



# Proccesing Prints | Final Result
print("Sum Of Even Numbers (While Loop):  " , get_sum_even_numbers_while(n))
print("  ")
print("Sum Of Even Numbers (For Loop):  ", get_sum_even_numbers_for(n))
print("  ")
print("Random Numbers:  ", random_generator(n))
print("  ")
print("Unique Random Numbers:   ", random_generator_unique(n))
print("  ")
print(f"{x} Random Numbers From Unique List Of {n} Numbers.")
