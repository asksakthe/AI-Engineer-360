import numpy as np
# Define the matrix dimensions
cycles = 5
tests = 50
# Define the range for random execution times (inclusive)
min_time = 5
max_time = 50
# Create the 5x50 matrix with random integers
# The randint() function takes the highest number as exclusive, so we add 1 to max_time
execution_times = np.random.randint(low=min_time, high=max_time+1 , size=(cycles, tests))
# Print the resulting matrix
#print(execution_times)
# Optionally, you can also print the shape of the matrix to verify dimensions
print("\nShape of the matrix:", execution_times.shape)

# Statistical Analysis
# o Calculate the average execution time per cycle.
print(np.mean(execution_times, axis=1))
# o Identify the test case with the maximum execution time in the entire dataset.
print(np.max(execution_times, axis=1))
# o Find the standard deviation of execution times for each cycle to measure 
print(np.std(execution_times, axis=1))

# Extract the first 10 test execution times from Cycle 1.
print(execution_times[0,:11])
# o Extract the last 5 test execution times from Cycle 5.
print(execution_times[4,-5:])
# o Extract every alternate test from Cycle 3.
print(execution_times[2,0::2])

# Arithmetic Operations
# o Perform element-wise addition and subtraction between Cycle 1 and Cycle 2.
a = np.sum(execution_times[0,:])
b = np.sum(execution_times[1,:])
print(f"Sum of Cycle 1 elements: {a}\nSum of Cycle 2 elements: {b}\nThe difference is: {a-b}")
# o Perform element-wise multiplication and division between Cycle 4 and Cycle 5.
c = execution_times[3,:]
d = execution_times[4,:]
Multi = np.multiply(c,d)
divi = np.divide(c,d)
print(f"product of Cycle 4 and Cycle 5 {Multi}\nThe Division output between these Cycle 4 and Cycle 5: {divi}")