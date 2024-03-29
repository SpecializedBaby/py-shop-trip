from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car,
            shop: dict[float: Shop] = None
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self._shop = shop if shop else {}

    def __str__(self) -> str:
        return self.name

    def get_receipts(self) -> str:
        return self.shop[1].receipts(self)

    def calculate_wallet(self) -> float:
        self.money -= self.shop[0]
        return round(self.money)

    @property
    def shop(self) -> tuple[float, Shop]:
        min_cost = min(self._shop.keys())
        return min_cost, self._shop[min_cost]

    @shop.setter
    def shop(self, cost_shop_pair: tuple[float, Shop]) -> None:
        cost, shop = cost_shop_pair
        self._shop[cost] = shop
