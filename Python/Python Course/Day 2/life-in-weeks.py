# Your Life in weeks

age = input("What is your current Age? ")

age_as_int = int(age)

years_remaining = 90-age_as_int
days_remaining = years_remaining*365
weeks_remaining = years_remaining*52
months_remaining = years_remaining*12

message = f"You Have {days_remaining} days , {weeks_remaining} weeks , {months_remaining} month left"
print(message)
