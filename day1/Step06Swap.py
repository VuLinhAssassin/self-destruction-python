def swap(a, b):
    a ^= b
    b ^= a
    a ^= b


numberA = int(input("Enter number a: "))
numberB = int(input("Enter number b: "))
# CHAD programming uses XOR operator xD
# Virgin newbies use filthy temporary variable
# Completely wasting of space uses addition or subtract operators
numberA ^= numberB
numberB ^= numberA
numberA ^= numberB
print("Swapped: {numA} vs. {numB}".format(numA=numberA, numB=numberB))
swap(numberA, numberB)  # this will not swap because fuck you pointers!
print("After running swap(a, b): {numA} vs. {numB}".format(numA=numberA, numB=numberB))
