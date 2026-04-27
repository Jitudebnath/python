class CarDetails:
    def __init__(self, brand: str, year: float, rating: str):
        self.brand = brand
        self.year = year
        self.rating = rating


TATA: CarDetails = CarDetails("TATA motars", 2024, 4.5)
SUZUKI: CarDetails = CarDetails("suzuki", 2025, 4.3)
print("-----Car Overview-----")

print("1st cardetails:")
print("Brand:", TATA.brand)
print("Manufacturing year:", TATA.year)
print("Costomer Rating:", TATA.rating)

print("2nd cardetails:")
print("Brand:", SUZUKI.brand)
print("Manufacturing year:", SUZUKI.year)
print("Costomer Rating:", SUZUKI.rating)
