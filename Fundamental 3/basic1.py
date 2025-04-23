is_old = True
is_licenced = True
if is_old and is_licenced:
    print("You are old")
elif is_licenced:
    print("You are not old")
else:
    print("You are not old and not licenced")

# Truthy and Falsy
is_old_1 = bool('Hello')
is_license_1 = bool(5)
is_license_2 = bool(0)
print(is_old_1)  # True
print(is_license_1)  # True
print(is_license_2)  # False