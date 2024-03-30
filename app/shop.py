import math

from typing import Any


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __str__(self) -> str:
        return f"{self.name}"

    def costs_for_trip_to_shop(self,
                               customer: Any,
                               fuel_price: float) -> float:
        return self._calculate_fuel_price(
            customer,
            fuel_price
        ) + self.calculate_cart_price(customer)

    def receipts(self, customer: Any) -> str:
        total_cost = self.calculate_cart_price(customer)
        purchase_info = "You have bought:\n"
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                price = self.products[product]
                cost = float(price * quantity)
                cost = int(cost) if cost.is_integer() else cost
                purchase_info += f"{quantity} {product}s for "
                purchase_info += f"{cost} dollars\n"
        purchase_info += f"Total cost is {total_cost} dollars\nSee you again!"
        return purchase_info

    def calculate_cart_price(self, customer: Any) -> float:
        cart_price = 0
        for product, quantity in customer.product_cart.items():
            cart_price += self.products[product] * quantity
        return cart_price

    def _calculate_fuel_price(self,
                              customer: Any,
                              fuel_price: float) -> float:
        fuel_needed = self._calculate_fuel_needed(
            customer.location,
            customer.car.fuel_consumption
        )
        return round((fuel_needed * fuel_price) * 2, 2)

    def _calculate_fuel_needed(self,
                               location: list,
                               fuel_consumption: float
                               ) -> float:
        return (self._calculate_distance(location) * fuel_consumption) / 100

    def _calculate_distance(self, customer_location: list) -> float:
        return math.hypot(
            self.location[0] - customer_location[0],
            self.location[1] - customer_location[1]
        )
