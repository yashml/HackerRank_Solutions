x = {"Red": 4/7, "Black": 3/7}
y = {"Red": 5/9, "Black": 4/9}
z = {"Red": 4/8, "Black": 4/8}

# Calculating probability of events
event_1 = x["Red"] * y["Red"] * z["Black"]
event_2 = x["Red"] * y["Black"] * z["Red"]
event_3 = x["Black"] * y["Red"] * z["Red"]

# Printing the probability
print(event_1 + event_2 + event_3)