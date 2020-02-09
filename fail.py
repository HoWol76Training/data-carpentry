rainfall_obs = [1.5, 2.3, 1.1, -5.1, 0.1]
total = 0.0
for v in rainfall_obs:
    assert v >= 0, "Rainfall Observations must not be negative"
    total = total + v

print(f"Total rainfall: {total}")
