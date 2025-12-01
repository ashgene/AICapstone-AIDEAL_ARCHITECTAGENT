
"""
Entry point for the Multi-Agent E-Commerce Deal Finder demo.

Usage (from project root):

    python main.py \
        --query "Apple Watch SE 2nd Gen 40mm Starlight" \
        --objective lowest_price \
        --output-json report.json

"""

import argparse
import json
from pathlib import Path

from agents.coordinator import CoordinatorAgent
from agents.search_synthesizer import SearchSynthesizerAgent
from agents.ecommerce_scraper import ECommerceScraperAgent
from agents.deal_comparator import DealComparatorAgent
from demo_data import load_demo_catalogs
from utils.formatting import render_markdown_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Multi-Agent E-Commerce Deal Finder"
    )
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="Client product request in natural language.",
    )
    parser.add_argument(
        "--objective",
        type=str,
        default="lowest_price",
        choices=["lowest_price", "fastest_delivery"],
        help="Optimization objective for the deal comparator.",
    )
    parser.add_argument(
        "--output-json",
        type=str,
        default=None,
        help="Path to save the final JSON report (optional).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Initialize agents
    search_agent = SearchSynthesizerAgent()
    scraper_agent = ECommerceScraperAgent(
        catalogs=load_demo_catalogs()
    )
    comparator_agent = DealComparatorAgent(
        objective=args.objective
    )
    coordinator = CoordinatorAgent(
        search_agent=search_agent,
        scraper_agent=scraper_agent,
        comparator_agent=comparator_agent,
    )

    # Run full workflow
    report = coordinator.run(args.query)

    # Print Markdown report to console
    md = render_markdown_report(report)
    print(md)

    # Optionally persist JSON
    if args.output_json:
        output_path = Path(args.output_json)
        output_path.write_text(
            json.dumps(report, indent=2), encoding="utf-8"
        )
        print(f"\nJSON report written to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
