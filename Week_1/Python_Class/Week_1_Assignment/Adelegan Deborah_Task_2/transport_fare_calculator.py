distance = float(input("How long is this journey in Kilometers?: "))
fare_per_km = float(input("How much is this the cost of one kilometre?: "))
total_fare = float(distance * fare_per_km)
print(f"The total amount of travelling {distance } kilometeres from Abuja Drive is {total_fare:.2f} kobo")