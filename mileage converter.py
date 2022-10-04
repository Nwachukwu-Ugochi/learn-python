print("How many kilometers did you run today?")
kms = input("Enter kilometers here: ")
miles = float(kms)/1.60934
miles = round(miles, 2)

print("Your {}km run was {}miles".format(kms,miles))

