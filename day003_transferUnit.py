value = float(input("value="))
unit = str(input("unit="))
if unit == "cm":
    print("%fcm is %fin" % (value, value / 2.54))
elif unit == "in":
    print("%fin is %fcm" % (value, value * 2.54))

