basic = float(input("Enter basic salary: "))

hra = 0.20 * basic
da = 0.10 * basic
pf = 0.12 * basic

gross = basic + hra + da
net = gross - pf

if net >= 80000:
    category = "High Earner"
elif net >= 50000:
    category = "Mid Earner"
else:
    category = "Low Earner"

print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("PF:", pf)
print("Gross Salary:", gross)
print("Net Salary:", net)
print("Category:", category)
