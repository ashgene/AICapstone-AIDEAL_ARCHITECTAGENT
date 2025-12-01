
"""
Domain model for a normalized product offer.

This represents the unified schema that the Scraper Agent
emits and the Deal Comparator consumes.
"""

from dataclasses import dataclass


@dataclass
class ProductOffer:
    platform: str
    product_name: str
    seller: str
    price: float
    shipping_cost: float
    currency: str
    estimated_delivery_days: int
    return_policy: str
    url: str

    @property
    def total_price(self) -> float:
        """Final price used in comparison (price + shipping)."""
        return self.price + self.shipping_cost
