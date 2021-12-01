from datetime import datetime
birth_date = int(input("Enter your year of birth: "))
current_date = datetime.now().year
result = current_date - birth_date
print(f" You are {result} years old ")