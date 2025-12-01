
# Design Write-Up: Multi-Agent E-Commerce Deal Finder

## 1. Problem Framing

Consumers face a fragmented marketplace with multiple e-commerce platforms, each with different pricing, shipping, and return policies. The task of finding the best overall deal is cognitively heavy and time-consuming. This project frames that challenge as a **multi-agent coordination problem**.

## 2. Architectural Objectives

The design targets four core objectives:

1. **Specialization** — Each agent owns a tightly scoped responsibility.
2. **Sequential orchestration** — A Coordinator Agent governs end-to-end flow.
3. **Data fusion** — Outputs are progressively refined across the pipeline.
4. **Extensibility** — The architecture can be upgraded to use LLMs and real APIs.

## 3. Agents and Responsibilities

- **Search Synthesizer Agent**
  - Input: Natural language client query.
  - Output: Multiple query variants for robust matching.
  - Role: Simulates LLM-style query optimization using rule-based transformations.

- **E-Commerce Scraper Agent**
  - Input: Search variants.
  - Output: List of normalized `ProductOffer` objects.
  - Role: Aggregates and normalizes cross-platform offers using mock demo catalogs.

- **Deal Comparator Agent**
  - Input: List of `ProductOffer`.
  - Output: Ranked list of offers + best deal + rationale.
  - Role: Applies explicit scoring logic based on objective (lowest price, fastest delivery).

- **Coordinator Agent**
  - Input: Client request.
  - Output: Fused report including best deal and markdown narrative.
  - Role: Orchestrates the call sequence and composes the final client-facing payload.

## 4. Data Flow

1. Client issues a product request.
2. Search Synthesizer generates search phrases.
3. Scraper filters demo catalogs and emits offers.
4. Comparator scores and ranks offers.
5. Coordinator produces JSON + Markdown outputs.

This linear pipeline preserves transparency and debuggability.

## 5. Extensibility Considerations

- Replace rule-based synthesis with LLM-backed semantic expansion.
- Replace mock catalogs with API connectors (Amazon, Flipkart, etc.).
- Add new agents for seller reputation, warranty analysis, and policy summarization.
- Introduce multi-criteria scoring or LLM-based rationale generation.

## 6. Conclusion

The system operationalizes core multi-agent concepts—**specialization**, **coordination**, and **data fusion**—on a realistic consumer use case: finding the best e-commerce deal with clear, auditable logic and an extensible architecture.
