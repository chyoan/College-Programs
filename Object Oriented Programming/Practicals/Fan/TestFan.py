from Fan import Fan

f1 = Fan(3, 10.0, "yellow", True)
f2 = Fan(2, 5.0, "blue", False)

print(f"Fan 1:\nSpeed: {f1.get_speed()}\nRadius: {f1.get_radius()}\nColor: {f1.get_color()}\nOn: {f1.get_on()}\n")
print(f"Fan 2:\nSpeed: {f2.get_speed()}\nRadius: {f2.get_radius()}\nColor: {f2.get_color()}\nOn: {f2.get_on()}")