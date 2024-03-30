import json

from app.gas_station import GasStation
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        date = json.load(file)
        gas_station = GasStation(date["FUEL_PRICE"])
        customers_date = date["customers"]
        shops_date = date["shops"]

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
            customer.add_shop_cost(costs, shop)
            print(f"{customer}'s trip to the {shop} costs {costs}")

        if not customer.enough_money():
            break
        print(f"{customer} rides to {customer.costs[1]}\n")
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer}, for your purchase!")
        print(customer.get_receipts() + "\n")
        print(f"{customer} rides home")
        print(f"{customer} now has {customer.calculate_wallet()} dollars\n")


if __name__ == "__main__":
    shop_trip()
