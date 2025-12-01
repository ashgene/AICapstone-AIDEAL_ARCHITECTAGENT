
"""
Demo catalogs for the E-Commerce Scraper Agent.

This module provides a small curated dataset that mimics offers
from Amazon, Flipkart, Myntra, Blinkit, Instamart, and Meesho.

The Scraper Agent uses this dataset to demonstrate cross-platform
aggregation and normalization without performing any real scraping.
"""

from typing import Dict, List

from models.product_offer import ProductOffer


def load_demo_catalogs() -> Dict[str, List[ProductOffer]]:
    """
    Returns demo catalogs keyed by platform name.

    You can extend this dataset to showcase richer scenarios or
    edge cases (multiple sellers, extreme shipping, etc.).
    """
    catalogs: Dict[str, List[ProductOffer]] = {}

    # Amazon
    catalogs["Amazon"] = [
        ProductOffer(
            platform="Amazon",
            product_name="Apple Watch SE (2nd Gen) 40mm GPS - Starlight",
            seller="AppStore Retail",
            price=27999.0,
            shipping_cost=0.0,
            currency="INR",
            estimated_delivery_days=3,
            return_policy="10-day replacement",
            url="https://www.amazon.example/apple-watch-se-2-40-starlight",
        ),
        ProductOffer(
            platform="Amazon",
            product_name="Bose QuietComfort Ultra Wireless Headphones - Black",
            seller="AudioWorld",
            price=34990.0,
            shipping_cost=99.0,
            currency="INR",
            estimated_delivery_days=4,
            return_policy="7-day return",
            url="https://www.amazon.example/bose-qc-ultra-black",
        ),
    ]

    # Flipkart
    catalogs["Flipkart"] = [
        ProductOffer(
            platform="Flipkart",
            product_name="Apple Watch SE 2nd Gen 40 mm GPS - Starlight",
            seller="SuperRetailer",
            price=27499.0,
            shipping_cost=49.0,
            currency="INR",
            estimated_delivery_days=2,
            return_policy="7-day replacement",
            url="https://www.flipkart.example/apple-watch-se-2-40-starlight",
        ),
        ProductOffer(
            platform="Flipkart",
            product_name="Bose QC Ultra Over-Ear Noise Cancelling Headphones (Black)",
            seller="PremiumAudioStore",
            price=34490.0,
            shipping_cost=0.0,
            currency="INR",
            estimated_delivery_days=2,
            return_policy="10-day return",
            url="https://www.flipkart.example/bose-qc-ultra-black",
        ),
    ]

    # Myntra
    catalogs["Myntra"] = [
        ProductOffer(
            platform="Myntra",
            product_name="Apple Watch SE 2 Aluminium Case 40mm - Starlight Sport Band",
            seller="MyntraTech",
            price=28199.0,
            shipping_cost=0.0,
            currency="INR",
            estimated_delivery_days=4,
            return_policy="15-day return",
            url="https://www.myntra.example/apple-watch-se-2-40-starlight",
        ),
        ProductOffer(
            platform="Myntra",
            product_name="Bose QuietComfort Ultra Headphones Wireless - Black",
            seller="AudioHub Myntra",
            price=35200.0,
            shipping_cost=0.0,
            currency="INR",
            estimated_delivery_days=3,
            return_policy="15-day return",
            url="https://www.myntra.example/bose-qc-ultra-black",
        ),
    ]

    # Blinkit
    catalogs["Blinkit"] = [
        ProductOffer(
            platform="Blinkit",
            product_name="Apple Watch SE 2 40mm GPS - Starlight (Quick Delivery)",
            seller="BlinkitElectro",
            price=28999.0,
            shipping_cost=0.0,
            currency="INR",
            estimated_delivery_days=1,
            return_policy="No-return, only DOA",
            url="https://www.blinkit.example/apple-watch-se-2-40-starlight",
        )
    ]

    # Instamart
    catalogs["Instamart"] = [
        ProductOffer(
            platform="Instamart",
            product_name="Bose QC Ultra Wireless Headphones - Black (Express)",
            seller="Instamart Audio",
            price=35990.0,
            shipping_cost=0.0,
            currency="INR",
            estimated_delivery_days=1,
            return_policy="3-day return",
            url="https://www.instamart.example/bose-qc-ultra-black",
        )
    ]

    # Meesho
    catalogs["Meesho"] = [
        ProductOffer(
            platform="Meesho",
            product_name="Apple Watch SE 2 (2nd Gen) 40mm Starlight GPS",
            seller="MeeshoTech",
            price=26999.0,
            shipping_cost=199.0,
            currency="INR",
            estimated_delivery_days=6,
            return_policy="7-day return",
            url="https://www.meesho.example/apple-watch-se-2-40-starlight",
        )
    ]

    return catalogs
