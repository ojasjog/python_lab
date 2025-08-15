import random

seats=random.randint(1,200)

while seats != 0:
	num_tickets = eval(input(f"Enter number of tickets you want to book (Total Seats = {seats}): "))

	if num_tickets>seats:
		print("Not enough seats available")
		break
	else:
		proceed = input("Are you sure you want to proceed?").lower()
		

		if proceed == "yes":
			newseats=seats-num_tickets
			seats=newseats

			if seats>0:
				print(f"Booking {num_tickets} tickets")
				print(f"Remaining Seats: {seats}")
			elif seats == 0:
				print(f"Remaining Seats: {seats}")
				print("All seats have been booked. Thank you !")
				break

			else:
				print("Not enough seats available.")
				break
		else:
			print("Thank you for using out Ticket Booking System!")
			break
