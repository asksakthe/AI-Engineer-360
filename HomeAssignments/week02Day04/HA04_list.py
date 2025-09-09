prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

mid_prime = prime_numbers[3:8]
print(mid_prime)

second_half = prime_numbers[1::2]
print(second_half)

negative_index = prime_numbers[-3:]
print(negative_index)

rev_List = prime_numbers[::-1]
print(rev_List)

sorted_List = sorted(prime_numbers, reverse=True)
print(sorted_List)