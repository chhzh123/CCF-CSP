n = int(input())
five = n // 50
three = (n - five * 50) // 30
ten = (n - five * 50 - three * 30) // 10
print(five * 7 + three * 4 + ten * 1)