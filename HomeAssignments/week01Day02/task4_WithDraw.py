Amt = int(input("Enter your Withdraw Amount: "))
def WithDrawAmount(Amt):
	if (Amt > 100):
		if (Amt%100) == 0:
			return f"Dispensing {Amt}"
		else:
			return f"Invalid amount"
	else:
		return f"Requested Amount Rs.{Amt} is below Rs.100, Dispense only multiples of 100" 


print(WithDrawAmount(Amt))