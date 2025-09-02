#User Input section
n = int(input("Enter your input: "))
#function definition
def FizzBizz(n:any):
		if (i%5) == 0 and (i%3) ==0:
			return f"FizzBuzz"
		elif(i%3) == 0:
			return f"Fizz"
		elif(i%5) == 0:
			return f"Buzz"
		else:
			return f"{i}"
		
#functional call
for i in range(1,n+1):
	func_call = FizzBizz(i)
	print(func_call)