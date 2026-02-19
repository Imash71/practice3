def greet_user(name, age=18):
   """Greets user with name and age."""
   print(f"Hello {name}, you are {age} years old.")
greet_user("Imash")      # использует возраст по умолчанию
greet_user("Ali", 20)