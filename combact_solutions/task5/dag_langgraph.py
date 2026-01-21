"""
Intro to DAG with LangGraph (Conditional Routing)

This module demonstrates a simple Directed Acyclic Graph (DAG) built using
LangGraph with conditional routing based on user input.

Purpose:
- To show understanding of control flow in LangGraph
- To demonstrate decision-based pipelines using a graph structure
- To route execution to different nodes based on input type

Logic Implemented:
- If the user input looks like a mathematical expression, route to a
  Calculator Node
- Otherwise, route to an LLM Node

Graph Structure:
    Router
      ├── Calculator Node ──▶ END
      └── LLM Node ─────────▶ END

Key Concepts Demonstrated:
- Conditional entry points in LangGraph
- Directed, acyclic execution flow
- Separation of concerns using nodes
- Explicit control flow handled by the graph (not Python if/else logic)

LLM Handling:
- A mock LLM is used to keep the demo fully offline and dependency-free
- Local LLM integration (e.g., Ollama) was explored but is not required
- The focus of this task is routing and DAG logic, not model quality

Testing:
- The script includes simple tests that trigger both the calculator path
  and the LLM path to verify correct routing

Note:
This implementation is intentionally minimal and educational, focused on understanding LangGraph fundamentals.
"""


from typing import TypedDict
from langgraph.graph import StateGraph, END

# Graph State

class GraphState(TypedDict):
    user_input: str
    response: str


# Mock LLM Node

def llm_node(state: GraphState) -> GraphState:
    state["response"] = f"(LLM) Response to: '{state['user_input']}'"
    return state



# Calculator Node

def calculator_node(state: GraphState) -> GraphState:
    try:
        result = eval(state["user_input"])
        state["response"] = f"Calculation result: {result}"
    except Exception:
        state["response"] = "Invalid calculation."
    return state



# Router Node

def router_node(state: GraphState) -> str:
    allowed_chars = set("0123456789+-*/(). ")

    if all(char in allowed_chars for char in state["user_input"]):
        return "calculator"
    return "llm"


# Build DAG

def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("calculator", calculator_node)
    graph.add_node("llm", llm_node)

    graph.set_conditional_entry_point(
        router_node,
        {
            "calculator": "calculator",
            "llm": "llm",
        },
    )

    graph.add_edge("calculator", END)
    graph.add_edge("llm", END)

    return graph.compile()


# Tests (Both Paths)

if __name__ == "__main__":
    app = build_graph()

    print("\nCalculator Path")
    print(app.invoke({"user_input": "10 * (2 + 3)", "response": ""})["response"])

    print("\n LLM Path ")
    print(app.invoke({"user_input": "What is LangGraph?", "response": ""})["response"])
