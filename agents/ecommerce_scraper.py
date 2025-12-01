
"""
E-Commerce Scraper Agent.

Responsibility:
- Take optimized search phrases.
- Query multiple e-commerce "sources".
- Return a unified list of ProductOffer objects.

In this educational project, we **mock** the external sources
using in-memory demo catalogs. This avoids any violation of
site terms-of-service while still demonstrating:

- Search fan-out per site.
- Data normalization into a standard schema.
- Multi-source aggregation.
"""

from typing import Dict, List

from .base import Agent
from models.product_offer import ProductOffer


class ECommerceScraperAgent(Agent):
    @property
    def name(self) -> str:
        return "ECommerceScraperAgent"

    def __init__(self, catalogs: Dict[str, List[ProductOffer]]):
        """
        :param catalogs: Mapping from platform name to a list of
                         ProductOffer entries (demo catalogs).
        """
        self.catalogs = catalogs

    def run(self, search_terms: List[str]) -> List[ProductOffer]:
        """
        Filter demo catalogs using the provided search terms.

        In a production implementation this method would:
        - Respect each site's robots.txt and terms of service.
        - Call official APIs or structured data endpoints where available.
        - Implement retry/backoff, rate limiting, and monitoring.

        :param search_terms: List of search strings from the
                             SearchSynthesizerAgent.
        :return: List of matching ProductOffer objects.
        """
        if not search_terms:
            return []

        results: List[ProductOffer] = []
        lowered_terms = [t.lower() for t in search_terms]

        for platform, offers in self.catalogs.items():
            for offer in offers:
                haystack = (
                    f"{offer.product_name} {offer.seller}"
                ).lower()
                if any(term in haystack for term in lowered_terms):
                    results.append(offer)

        return results
