
"""
Search Synthesizer Agent.

Responsibility:
- Receive a natural language product request.
- Generate multiple optimized search strings / variants
  suitable for downstream e-commerce queries.

In a production setting this could call an LLM (e.g., Gemini).
Here we implement lightweight heuristics to keep the project
self-contained and runnable without external APIs.
"""

from typing import List, Set

from .base import Agent


class SearchSynthesizerAgent(Agent):
    @property
    def name(self) -> str:
        return "SearchSynthesizerAgent"

    def run(self, client_query: str) -> List[str]:
        """
        Generate multiple search term variants from a client request.

        :param client_query: Free-form natural language product request.
        :return: List of optimized search strings.
        """
        normalized = client_query.strip()
        if not normalized:
            raise ValueError("Client query is empty.")

        variants: Set[str] = set()

        # 1. Raw query
        variants.add(normalized)

        # 2. Lowercased
        lower = normalized.lower()
        variants.add(lower)

        # 3. Remove common filler words
        filler = {
            "best",
            "deal",
            "cheap",
            "cheapest",
            "offer",
            "online",
            "price",
            "discount",
        }
        tokens = [t for t in lower.split() if t not in filler]
        compact = " ".join(tokens)
        if compact:
            variants.add(compact)

        # 4. Very naive brand/product normalizations
        replacements = {
            "iwatch": "apple watch",
            "qc": "quietcomfort",
        }
        normalized_tokens = [
            replacements.get(t, t) for t in tokens
        ]
        normalized_phrase = " ".join(normalized_tokens)
        if normalized_phrase:
            variants.add(normalized_phrase)

        # 5. De-duplicate and return as list
        return list(variants)
