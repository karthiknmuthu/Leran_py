print("Welcome to tip calculator")
bill = float((input("Whta is the total amount : ")))
tip_persecnt = int(
    input("what is the percentage of tip you would like to give :10,12,15"))
plp = int(input("how many people to split the bill : "))
Total_Bill = tip_persecnt / 100 * bill + bill
final_amount = Total_Bill / plp
print(f"Each person sholud pay {final_amount}")
print(Total_Bill)
