
# Multi-Agent E-Commerce Deal Finder  
*A Demonstration of Specialization, Coordination, and Multi-Agent Orchestration*

## Overview

This project implements an end-to-end **Multi-Agent E-Commerce Deal Finder**, engineered to automate a complex, high-value consumer workflow: finding the **best deal** for any product across multiple online commerce platforms.

The system demonstrates **specialized agents**, **sequential orchestration**, and **data fusion**, aligning directly with modern enterprise-grade agentic architectures.

## Key Capabilities

| Agent | Role | Output |
|------|------|---------|
| **Search Synthesizer Agent** | Expands free-form queries into optimized search strings. | Search phrases, variants, canonicalized forms. |
| **E-Commerce Scraper Agent** | Gathers structured product offers from multiple “sites” (mock data). | Normalized `ProductOffer` objects. |
| **Deal Comparator Agent** | Computes final price, delivery, ranking, and best-deal rationale. | Ranked offer list + recommended deal. |
| **Coordinator Agent** | Orchestrates the workflow and compiles the final report. | A client-facing JSON + Markdown summary. |

## Project Structure

```text
multi_agent_deal_finder/
├── main.py
├── agents/
│   ├── base.py
│   ├── search_synthesizer.py
│   ├── ecommerce_scraper.py
│   ├── deal_comparator.py
│   └── coordinator.py
├── models/
│   └── product_offer.py
├── utils/
│   └── formatting.py
└── demo_data.py
```

## Installation

This project uses only Python’s standard library.

```bash
git clone <YOUR-REPO-URL>
cd multi_agent_deal_finder
python main.py --help
```

## How to Run

```bash
python main.py \
  --query "Apple Watch SE 2nd Gen 40mm Starlight" \
  --objective lowest_price
```

```bash
python main.py \
  --query "Bose QC Ultra in black" \
  --objective fastest_delivery
```

Save JSON output:

```bash
python main.py \
  --query "Apple Watch SE" \
  --objective lowest_price \
  --output-json report.json
```

## Extensibility

The architecture is intentionally modular so you can:

- Replace search synthesis with an LLM.
- Swap the mock scraper with real commerce APIs.
- Enhance the comparator with multi-criteria decision-making or LLM judgment.
