"""Original, intentionally unstructured invoice program for Practical 4."""

items = [
    ("Notebook", 120.0, 2),
    ("Pen pack", 80.0, 1),
    ("Backpack", 300.0, 1),
]

sub = 0
for i in items:
    sub = sub + i[1] * i[2]

if sub >= 500:
    disc = sub * 0.10
else:
    disc = 0

after_disc = sub - disc
tax = after_disc * 0.08
total = after_disc + tax

print("INVOICE")
for i in items:
    print(f"{i[0]} x {i[2]}: INR {i[1] * i[2]:.2f}")
print(f"Subtotal: INR {sub:.2f}")
print(f"Discount: INR {disc:.2f}")
print(f"Tax: INR {tax:.2f}")
print(f"Total: INR {total:.2f}")
