# LangGraph DAG – Conditional Routing Demo

## Project Overview

This project demonstrates a **Directed Acyclic Graph (DAG)** built using **LangGraph**, showcasing how execution flow can be controlled through **conditional routing** instead of traditional `if/else` logic.

The implementation is intentionally minimal and educational, focusing on understanding **LangGraph fundamentals**, graph-based control flow, and decision-driven pipelines.

---

## Objective

* Understand how DAGs work in LangGraph
* Learn conditional entry points and routing
* Separate logic into independent graph nodes
* Build a clean, testable control-flow pipeline

---

## What This Project Does

* Accepts a user input string
* Routes execution based on input type:

  * **Mathematical expression** → Calculator Node
  * **General text** → Mock LLM Node
* Executes exactly one path in the DAG
* Returns a final response and terminates

---

## Graph Structure

```
        Router
          │
          ├── Calculator Node ──▶ END
          │
          └── LLM Node ─────────▶ END
```

---

## Key Concepts Demonstrated

* Directed Acyclic Graph (DAG) execution
* Conditional entry points in LangGraph
* Explicit control flow handled by the graph
* Separation of concerns using nodes
* Deterministic, single-path execution

---

## Node Description

### Router Node

* Inspects the user input
* Checks whether the input looks like a mathematical expression
* Routes execution to the appropriate node

### Calculator Node

* Evaluates mathematical expressions using Python
* Returns calculation results or an error message

### LLM Node (Mock)

* Simulates an LLM response
* Keeps the project fully offline and dependency-light
* Emphasizes routing logic rather than model quality

---

## LLM Handling

* A **mock LLM** is used for simplicity
* No external APIs or internet access required
* Local LLMs (e.g., Ollama) were explored but are not necessary
* Focus remains on **graph routing**, not language generation quality

---

## Project Structure

```
.
├── dag_langgraph.py
└── README.md
```

---

## How to Run

### Prerequisites

* Python 3.9+
* `langgraph` installed

### Run the Script

```bash
python dag_langgraph.py
```

---

## Sample Output

```
Calculator Path
Calculation result: 50

LLM Path
(LLM) Response to: 'What is LangGraph?'
```

---

## Testing

The script includes built-in tests that:

* Trigger the calculator path using a math expression
* Trigger the LLM path using a natural language question

This confirms correct routing and DAG execution.

---

## Notes

* This project is designed for learning and interviews
* The DAG is deterministic and acyclic by design
* Logic routing is handled by LangGraph, not Python conditionals
* Ideal as a foundational example for agent workflows and pipelines

---


