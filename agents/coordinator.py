
"""
Coordinator Agent.

Responsibility:
- Orchestrate the end-to-end workflow:
    1. Receive client request.
    2. Invoke SearchSynthesizerAgent.
    3. Invoke ECommerceScraperAgent.
    4. Invoke DealComparatorAgent.
    5. Aggregate all outputs into a final report.

This is the "brain" of the system and is responsible for
sequential execution, state passing, and data fusion.
"""

from typing import Any, Dict

from .base import Agent
from .search_synthesizer import SearchSynthesizerAgent
from .ecommerce_scraper import ECommerceScraperAgent
from .deal_comparator import DealComparatorAgent


class CoordinatorAgent(Agent):
    @property
    def name(self) -> str:
        return "CoordinatorAgent"

    def __init__(
        self,
        search_agent: SearchSynthesizerAgent,
        scraper_agent: ECommerceScraperAgent,
        comparator_agent: DealComparatorAgent,
    ):
        self.search_agent = search_agent
        self.scraper_agent = scraper_agent
        self.comparator_agent = comparator_agent

    def run(self, client_request: str) -> Dict[str, Any]:
        """
        Execute the complete multi-agent pipeline.

        :param client_request: User's natural language product request.
        :return: Structured report combining all intermediate outputs.
        """
        # Step 1: Search synthesis
        search_terms = self.search_agent.run(client_request)

        # Step 2: Scrape e-commerce platforms (mocked)
        offers = self.scraper_agent.run(search_terms)

        # Step 3: Compare deals
        comparison = self.comparator_agent.run(offers)

        # Final fused report
        report: Dict[str, Any] = {
            "original_request": client_request,
            "search_terms": search_terms,
            "num_offers_found": len(comparison["ranked_offers"]),
            "deal_objective": comparison["objective"],
            "ranked_offers": comparison["ranked_offers"],
            "best_deal": comparison["best_deal"],
            "rationale": comparison["rationale"],
        }
        return report
