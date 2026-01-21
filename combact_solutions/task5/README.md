# Intro to DAG with LangGraph

## Overview
This project demonstrates a **Directed Acyclic Graph (DAG)** built using **LangGraph** with **conditional routing**.

The goal is to show how a graph can make decisions and route execution to different nodes based on input, instead of using traditional `if/else` logic in a script.



## What This Task Demonstrates
- DAG-based control flow using LangGraph
- Conditional routing inside a graph
- Decision-based AI pipelines
- Multiple execution paths in a single workflow

The graph routes input as follows:
- If the input is a calculation → **Calculator Node**
- Otherwise → **LLM Node**



## Learning Context (Important)
I was **new to the concept of DAGs** and LangGraph when working on this task.

Because DAG-based execution and routing were unfamiliar concepts, some parts of the implementation were **vibe coded** — meaning:
- I experimented with graph structure and node flow
- I tried different routing setups to understand how LangGraph behaves
- I learned by running the graph and observing which path was taken

This approach helped me understand:
- How routing works in a DAG
- How nodes are connected and executed
- How control flow is managed by the graph itself



## Vibe Coding for Learning
The following parts were intentionally vibe coded for **experimentation and learning purposes**:
- **Router Node** – to understand conditional entry points
- **Calculator Node** – to explore branching logic inside a DAG

The final structure is simple, but it reflects hands-on learning rather than pre-designed architecture.



## Graph Logic

### Routing Rule
- If input contains only numbers and math operators → Calculator Node
- Else → LLM Node

### Graph Flow
Router
├── Calculator Node → END
└── LLM Node → END

This graph is **directed and acyclic**, satisfying DAG constraints.



## Why a Mock LLM Is Used
A mock LLM is used because:
- The task focuses on routing and control flow
- API keys or local LLM setup should not block learning
- The goal was to understand LangGraph, rather than  model quality

The LLM node simply represents a non-calculation processing path.



## Testing
The script includes simple tests to verify:
- Calculator path works for math inputs
- LLM path works for non-math inputs

This confirms that conditional routing behaves correctly.



## Limitations
- No real LLM responses
- No advanced math parsing
- Simple routing logic
These limitations are intentional to keep the focus on DAG fundamentals.



## Conclusion
This task helped me learn:
- How DAGs work in practice
- How LangGraph handles control flow
- How conditional routing replaces traditional scripting logic