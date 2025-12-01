
"""
Utilities for rendering final outputs (Markdown, etc.).
"""

from typing import Any, Dict, List


def _render_offers_table(
    offers: List[Dict[str, Any]]
) -> str:
    if not offers:
        return "_No offers found._\n"

    headers = [
        "Rank",
        "Platform",
        "Product",
        "Seller",
        "Price",
        "Shipping",
        "Total",
        "Currency",
        "ETA (days)",
        "Return Policy",
    ]

    # Build table header
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    # Add rows
    for offer in offers:
        row = [
            str(offer["rank"]),
            offer["platform"],
            offer["product_name"],
            offer["seller"],
            f"{offer['price']:.2f}",
            f"{offer['shipping_cost']:.2f}",
            f"{offer['total_price']:.2f}",
            offer["currency"],
            str(offer["estimated_delivery_days"]),
            offer["return_policy"],
        ]
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines) + "\n"


def render_markdown_report(report: Dict[str, Any]) -> str:
    """
    Produce a client-facing Markdown summary of the workflow.

    :param report: Final fused report from the CoordinatorAgent.
    :return: Markdown string.
    """
    lines: List[str] = []

    lines.append("# Multi-Agent E-Commerce Deal Finder Report\n")

    # Original Request
    lines.append("## 1. Original Request\n")
    lines.append(f"> {report['original_request']}\n")

    # Search terms
    lines.append("## 2. Optimized Search Terms\n")
    for term in report["search_terms"]:
        lines.append(f"- `{term}`")
    lines.append("")

    # Summary of offers
    lines.append("## 3. Offers Found\n")
    lines.append(
        f"- Total offers considered: **{report['num_offers_found']}**"
    )
    lines.append(
        f"- Optimization objective: **{report['deal_objective']}**\n"
    )

    lines.append(_render_offers_table(report["ranked_offers"]))

    # Best deal
    lines.append("## 4. Recommended Deal\n")
    best = report["best_deal"]
    if best is None:
        lines.append("_No recommendation available (no offers found)._")
    else:
        lines.append(
            f"- **Platform:** {best['platform']}\n"
            f"- **Product:** {best['product_name']}\n"
            f"- **Seller:** {best['seller']}\n"
            f"- **Total Price:** {best['total_price']:.2f} {best['currency']} "
            f"(Item: {best['price']:.2f} + Shipping: {best['shipping_cost']:.2f})\n"
            f"- **ETA:** {best['estimated_delivery_days']} days\n"
            f"- **Return Policy:** {best['return_policy']}\n"
            f"- **URL:** {best['url']}\n"
        )

    # Rationale
    lines.append("## 5. Rationale\n")
    lines.append(report["rationale"] + "\n")

    # System-level explanation (for the course / instructor)
    lines.append("## 6. Multi-Agent Workflow Trace\n")
    lines.append(
        "- CoordinatorAgent orchestrated the workflow and assembled this report.\n"
        "- SearchSynthesizerAgent expanded the client request into multiple search terms.\n"
        "- ECommerceScraperAgent (mock) queried normalized demo catalogs for each platform.\n"
        "- DealComparatorAgent scored and ranked all offers according to the selected objective.\n"
    )

    return "\n".join(lines)
