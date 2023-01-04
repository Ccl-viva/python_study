total_price = int(input("what is the total fees"))
num_peo = int(input("how many people"))
tip_rate = float(input("tip rate"))

print(total_price*(1+ tip_rate) / num_peo)

