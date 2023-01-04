# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
name = lower(name)

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

print(f"T occurs {t} times")
print(f"R occurs {r} times")
print(f"U occurs {u} times")
print(f"E occurs {e} times")
total1 = t + r + u + e
print(f"Total = {total}")
print(f"L occurs {l} times")
print(f"O occurs {o} times")
print(f"V occurs {v} times")
print(f"E occurs {e} times")
total2 = l + o + v + e
print(f"Total = {total2}")

print("Your score is" + total1*10 + total2)






