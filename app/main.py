from datetime import datetime
import json

from app.gas_station import GasStation
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json") as file:
        date = json.load(file)
        fuel_price_date = date["FUEL_PRICE"]
        customers_date = date["customers"]
        shops_date = date["shops"]

    gas_station = GasStation(fuel_price_date)

    for customer in customers_date:
        customer = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops_date:
            shop = Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
            costs = shop.costs_for_trip_to_shop(customer, gas_station.price)
            customer.shop = (costs, shop)
            print(f"{customer}'s trip to the {shop} costs {costs}")
        print(f"{customer} rides to {customer.shop[1]}\n")

        print("Date: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer}, for your purchase!")
        print(customer.get_receipts() + "\n")
        print(f"{customer} rides home")
        print(f"{customer} now has {customer.calculate_wallet()} dollars\n")


if __name__ == "__main__":
    shop_trip()
