
"""
Deal Comparator Agent.

Responsibility:
- Receive a set of ProductOffer instances.
- Compute a "final price" and other metrics.
- Rank offers according to an optimization objective.
- Provide a structured list of ranked deals.

Objectives implemented in this prototype:
- 'lowest_price': minimize total price (price + shipping).
- 'fastest_delivery': prioritize earliest delivery, then price.
"""

from typing import Any, Dict, List

from .base import Agent
from models.product_offer import ProductOffer


class DealComparatorAgent(Agent):
    @property
    def name(self) -> str:
        return "DealComparatorAgent"

    def __init__(
        self,
        objective: str = "lowest_price",
    ):
        if objective not in {"lowest_price", "fastest_delivery"}:
            raise ValueError(
                f"Unsupported objective: {objective}"
            )
        self.objective = objective

    # --- internal scoring logic -----------------------------------------

    def _score(self, offer: ProductOffer) -> float:
        """
        Internal scoring function depending on objective.

        Lower scores are better.

        This is intentionally simple and transparent for teaching.
        """
        if self.objective == "lowest_price":
            return offer.total_price

        if self.objective == "fastest_delivery":
            # Weighted combination:
            #   - Delivery dominates.
            #   - Price breaks ties.
            return (
                offer.estimated_delivery_days * 10.0
                + offer.total_price / 1000.0
            )

        # Fallback: treat as lowest_price
        return offer.total_price

    # --- public API ------------------------------------------------------

    def run(
        self, offers: List[ProductOffer]
    ) -> Dict[str, Any]:
        """
        Rank product offers and produce an analysis payload.

        :param offers: List of ProductOffer from the scraper.
        :return: Dict containing ranked offers and an overall rationale.
        """
        if not offers:
            return {
                "objective": self.objective,
                "ranked_offers": [],
                "best_deal": None,
                "rationale": "No offers found.",
            }

        ranked = sorted(offers, key=self._score)

        ranked_serialized: List[Dict[str, Any]] = []
        for idx, offer in enumerate(ranked, start=1):
            ranked_serialized.append(
                {
                    "rank": idx,
                    "platform": offer.platform,
                    "product_name": offer.product_name,
                    "seller": offer.seller,
                    "price": offer.price,
                    "shipping_cost": offer.shipping_cost,
                    "total_price": offer.total_price,
                    "currency": offer.currency,
                    "estimated_delivery_days": offer.estimated_delivery_days,
                    "return_policy": offer.return_policy,
                    "url": offer.url,
                }
            )

        best = ranked_serialized[0]

        if self.objective == "lowest_price":
            rationale = (
                f"Selected the offer with the lowest total price "
                f"({best['total_price']} {best['currency']}) "
                f"across all platforms."
            )
        elif self.objective == "fastest_delivery":
            rationale = (
                "Selected the offer with the fastest estimated delivery "
                f"({best['estimated_delivery_days']} days), using total "
                "price as a tie-breaker."
            )
        else:
            rationale = "Selected best deal according to configured objective."

        return {
            "objective": self.objective,
            "ranked_offers": ranked_serialized,
            "best_deal": best,
            "rationale": rationale,
        }
