# Your life in weeks: a 90-year human life in years 
age = input("What is your current age?")
# 🚨 Don't change the code below 👇 
 

#Write your code below this line 👇 
age_as_int = int(age);
years_remaining = 90 - age_as_int;
days_remaining = years_remaining * 365;
weeks_remaining = years_remaining * 52; 
months_remaining = years_remaining * 12;
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.");
 
