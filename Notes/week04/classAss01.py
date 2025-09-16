import numpy as np
#
oneDim = np.array([10,20,30,40,50,60])

print("Assignment 1 output")
print("------------------------")
print(type(oneDim))
print(oneDim[2:])
print(oneDim[3:5])
print(oneDim[-4])
print(oneDim[-1])

sample_twoDim = np.array([[21,23,25,27],[41,43,45,47],[4,6,7,8]])
print("Assignment 2 output")
print("------------------------")
print(sample_twoDim[1,:])
print(sample_twoDim[0][1])
print(sample_twoDim[1][1])
print(sample_twoDim[0][3])
#sum of all elements in 2-D array
count_2D = 0
for i in sample_twoDim:
    for j in i:
        count_2D += j

print(f"Sum of all 2-Dimensional elements: {count_2D}")

sample_threeDim = np.array([[[21,23,25],[41,43,45]],[[31,33,35],[51,53,55]]])
print("Assignment 3 output :-")
print("------------------------")
print(sample_threeDim[0,0,:-1])
print(sample_threeDim[0][0][0])
print(sample_threeDim[0][1][2])
print(sample_threeDim[1][1][2])




