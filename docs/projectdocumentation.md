# Multi-Agent Content Generation System

### Author: Utkarsh Agarwal

---

## 1. Problem Statement

Product content creation is often manual, repetitive, and inconsistent across pages (FAQ, product descriptions, and comparison sheets).  
Brands and ecommerce platforms need automated tools that can convert raw product data into structured content that is ready to publish in multiple formats.

The goal is to design a **modular agentic automation system** that:

- reads raw product dataset
- understands and structures the data
- automatically generates user questions
- applies reusable content logic blocks
- assembles multiple types of content pages
- produces clean machine-readable JSON output

---

## 2. Solution Overview

The project implements a **multi-agent orchestration pipeline** that transforms raw product data into formatted output pages.  
The system contains independent agents, each performing a single responsibility and passing clean data to the next stage, demonstrating production style automation.

The pipeline produces:

- FAQ Page (`faq.json`)
- Product Description Page (`product_page.json`)
- Comparison Page (`comparison_page.json`)

All pages are automatically generated and stored in JSON format inside the `output/` directory.

---

## 3. Scope & Assumptions

### Scope

- Works on small structured product datasets
- Generates at least 15 categorized questions automatically
- Supports modular text blocks for flexible page assembly
- Uses fictional Product B for comparison mode

### Assumptions

- No external research or data sources are used
- Only provided dataset is allowed as input
- JSON is the final delivery format
- No UI or frontend is required (not within scope)

---

## 4. System Design

### 4.1 Architecture Flow

Raw Product Data
↓
Parser Agent
↓
Question Agent
↓
Logic Agent
↓
Template Agent
↓
JSON Output Agent
↓
Final JSON Pages

### 4.2 Agent Responsibilities

| Agent           | Responsibility                                     | Input              | Output                                                  |
| --------------- | -------------------------------------------------- | ------------------ | ------------------------------------------------------- |
| ParserAgent     | Converts raw text into internal product model      | raw input          | structured dict                                         |
| QuestionAgent   | Generates 15+ categorized questions                | product model      | grouped questions                                       |
| LogicAgent      | Produces reusable content logic blocks             | product model      | formatted blocks                                        |
| TemplateAgent   | Assembles content into structured page definitions | blocks + questions | page objects                                            |
| JSONOutputAgent | Writes final formatted pages into JSON files       | page objects       | `faq.json`, `product_page.json`, `comparison_page.json` |
| Orchestrator    | Controls pipeline execution order                  | none               | end-to-end automation                                   |

---

## 5. Orchestrator Workflow

instantiate agents →
parse product →
generate questions →
generate logic blocks →
build templates →
export JSON →
store files under /output

This ensures clarity, modularity, and extensibility, avoiding a monolithic single-script system.

---

## 6. Example Output Files

- `output/faq.json`
- `output/product_page.json`
- `output/comparison_page.json`

All pages confirm:

- clean JSON structure
- reusable sections
- agent-driven execution

---

## 7. Conclusion

This project demonstrates an extensible and modular multi-agent content automation workflow that transforms raw product information into independently usable formatted pages.

The design reflects:

- well-defined agent boundaries
- scalable and reusable architecture
- automated structured data generation
