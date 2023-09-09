def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    t= d.replace("$"," ")
    t1 = t.strip()
    r = float(t1)
    return (r)
def percent_to_float(p):
    tp= p.replace("%"," ")
    tp1 = tp.strip()
    floatP = float(tp1)
    return floatP/100

main()
