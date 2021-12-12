myName = input("What is your name? ")
myAge = int(input("How old are you? "))
# At least you can put that damn .format in a new line
print("So, your name is {name} and you are now {age} years old"
      .format(name=myName, age=myAge)
      )
