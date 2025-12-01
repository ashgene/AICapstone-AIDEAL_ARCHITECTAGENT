# AICapstone-AIDEAL_ARCHITECTAGENT
The AI Deal Architect: Multi-Agent E-Commerce Price Synthesis

# **Multi-Agent E-Commerce Deal Finder**

*A Demonstration of Specialization, Coordination, and Multi-Agent Orchestration*

---

## **Overview**

This project implements an end-to-end **Multi-Agent E-Commerce Deal Finder**, engineered to automate a complex, high-value consumer workflow: finding the **best deal** for any product across multiple online commerce platforms.

The system demonstrates **specialized agents**, **sequential orchestration**, and **data fusion**, aligning directly with modern enterprise-grade agentic architectures (as taught in Google’s AI Agents Intensive).

---

## **Key Capabilities**

| Agent                        | Role                                                                 | Output                                         |
| ---------------------------- | -------------------------------------------------------------------- | ---------------------------------------------- |
| **Search Synthesizer Agent** | Expands free-form queries into optimized search strings.             | Search phrases, variants, canonicalized forms. |
| **E-Commerce Scraper Agent** | Gathers structured product offers from multiple “sites” (mock data). | Normalized `ProductOffer` objects.             |
| **Deal Comparator Agent**    | Computes final price, delivery, ranking, and best-deal rationale.    | Ranked offer list + recommended deal.          |
| **Coordinator Agent**        | Orchestrates the workflow and compiles the final report.             | A client-facing JSON + Markdown summary.       |

The architecture is modular, extensible, and compliant with responsible AI practices (no real scraping; uses mock catalogs).

---

## **Project Structure**

```
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

---

## **Installation**

This project uses only Python’s standard library.

```bash
git clone <YOUR-REPO-URL>
cd multi_agent_deal_finder
python main.py --help
```

---

## **How to Run**

### **Example 1 — Apple Watch Deal Finder**

```bash
python main.py \
  --query "Apple Watch SE 2nd Gen 40mm Starlight" \
  --objective lowest_price
```

### **Example 2 — Bose QC Ultra Best Delivery**

```bash
python main.py \
  --query "Bose QC Ultra in black" \
  --objective fastest_delivery
```

### **Save JSON Output**

```bash
python main.py \
  --query "Apple Watch SE" \
  --objective lowest_price \
  --output-json report.json
```

---

## **Example Markdown Output (Truncated)**

```
# Multi-Agent E-Commerce Deal Finder Report

## 1. Original Request
> Apple Watch SE 2nd Gen 40mm Starlight

## 2. Optimized Search Terms
- `apple watch se 2 40mm starlight`
- `apple watch se (2nd gen) 40mm gps starlight`
...

## 4. Recommended Deal
- Platform: Flipkart
- Total Price: 27548 INR
- ETA: 2 days
```

---

## **Extensibility**

This system is intentionally designed as a platform-level architecture:

* Replace search synthesizer with **Gemini or PaLM** for semantic reformulation.
* Replace scraper with **real API connectors** (e.g., Amazon Product API).
* Extend comparator with **LLM-based multi-criteria decision-making**.
* Add seller-reputation, warranty-score, and reliability-scoring agents.

---

## **License**

MIT License.

---

# 🎯 Design Write-Up (for course submission)

Save as: `DESIGN_WRITEUP.md`

---

# **Design Write-Up: Multi-Agent E-Commerce Deal Finder**

## **1. Problem Framing**

Consumers face a fragmented marketplace, navigating numerous e-commerce platforms to compare pricing, shipping, discounts, and delivery constraints. This problem naturally decomposes into **search optimization**, **multi-source retrieval**, and **comparative evaluation**—making it ideal for a multi-agent architecture.

---

## **2. Architectural Objectives**

The project was designed to demonstrate four key agentic principles emphasized in the Google AI Agents Intensive:

### **(1) Specialization**

Each agent embodies a narrow, domain-specific capability:

| Agent              | Specialization                                 |
| ------------------ | ---------------------------------------------- |
| Search Synthesizer | Query decomposition + variant generation       |
| E-Commerce Scraper | Multi-source structured data extraction (mock) |
| Deal Comparator    | Price/delivery optimization logic              |
| Coordinator        | Orchestration and state management             |

Each agent is cohesive and single-purpose, adhering to SOLID principles.

---

### **(2) Delegation and Sequential Orchestration**

The **Coordinator Agent** operates as the executive controller:

1. Receives client task.
2. Delegates to Search Synthesizer.
3. Passes outputs to Scraper.
4. Orchestrates data into Comparator.
5. Synthesizes final deliverable.

This illustrates how multi-agent systems pass state **downstream**, reducing ambiguity and enforcing deterministic flow.

---

### **(3) Data Fusion Across Agents**

The system demonstrates layered, progressive data refinement:

* **Natural language → Tokenized variants → Normalized product strings**
* **Unstructured catalog → Unified `ProductOffer` schema**
* **Raw prices + shipping + ETA → Final score + ranking**

This mirrors enterprise architectures where agents perform **extract-transform-decide** cycles.

---

### **(4) Extensibility and Modularity**

The architecture is built for evolution:

* Agent interfaces defined via `Agent` base class.
* Swappable implementations (e.g., LLM-based comparator).
* Catalog abstraction allows replacement with real APIs.
* Single-responsibility design reduces coupling risk.

This reflects industry expectations for scalable agent systems.

---

## **3. Design Rationale by Agent**

### **Search Synthesizer Agent**

* Implements heuristic linguistic transformations.
* Models how an LLM would generate optimized search variants.
* Ensures broader match coverage across inconsistent platform nomenclature.

### **E-Commerce Scraper Agent**

* Abstracts retrieval using `demo_data` catalogs.
* Normalizes output into a consistent schema.
* Demonstrates multi-source aggregation while avoiding TOS violations.

### **Deal Comparator Agent**

* Encapsulates all evaluative logic.
* Produces deterministic, auditable decision scores.
* Supports two optimization objectives:

  * Lowest total price
  * Fastest delivery
* Designed to be replaceable with a policy-driven LLM agent or multi-criteria decision analysis (MCDA) model.

### **Coordinator Agent**

* Central orchestrator enforcing workflow consistency.
* Produces a final, unified report consumable by clients or downstream systems.
* Demonstrates how agent outputs can be composed into structured artifacts (JSON/Markdown).

---

## **4. Data Flows**

```
Client Request
    ↓
Search Synthesizer Agent
    (Generate variants)
    ↓
E-Commerce Scraper Agent
    (Aggregate offers)
    ↓
Deal Comparator Agent
    (Rank and justify)
    ↓
Coordinator Agent
    (Final Report)
```

This strict pipeline architecture ensures:

* Deterministic outputs
* Debuggability
* Transparent scoring and reproducibility

---

## **5. Engineering Considerations**

### **No External Dependencies**

Ensures reproducibility, safety, and ease of demonstration.

### **Mock Catalogs**

Serve as proxies for real platforms, enabling:

* Controlled experiments
* Deterministic behaviour
* Ethical compliance

### **Normalized Domain Model (`ProductOffer`)**

Ensures all platforms produce data in a uniform contract, enabling fair comparison.

---

## **6. Evaluation Criteria**

The system meets the following agentic benchmarks:

| Criterion                      | Achieved By                                    |
| ------------------------------ | ---------------------------------------------- |
| **Specialized agents**         | Each module has a singular responsibility.     |
| **Inter-agent communication**  | Coordinator orchestrates sequential data flow. |
| **Data fusion**                | Scraper + Comparator pipeline.                 |
| **Autonomous decision-making** | Comparator ranks deals and outputs rationale.  |
| **Extensibility**              | Pluggable agents + clean abstractions.         |
| **Client-facing outputs**      | Structured JSON + Markdown reporting.          |

---

## **7. Future Extensions**

1. **LLM-Powered Query Expansion**

   * Semantic parsing
   * Canonicalization
   * Multi-lingual support

2. **Real Commerce APIs**

   * Amazon Advertising API
   * Flipkart Product Feed API

3. **LLM-Based Comparator**

   * Subjective ranking (brand value, warranty trust, return reliability)

4. **Additional Agents**

   * Seller Reputation Agent
   * Warranty/Policy Analyzer Agent
   * Price Prediction Agent (time series forecasting)

---

## **8. Conclusion**

This project is a fully functional demonstration of a **multi-agent AI system** built with clarity, specialization, and orchestration. It showcases how agentic systems can automate a real-world, high-value task—**finding the best e-commerce deal**—while demonstrating the architectural patterns taught in the Google AI Agents Intensive.

---
