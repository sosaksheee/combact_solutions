"""
Simple Interactive Chatbot using LangGraph

This module implements a minimal terminal-based chatbot using LangGraph to
demonstrate conversational memory and graph-based control flow.

Purpose:
- To learn how LangGraph represents logic as a graph instead of a linear script
- To understand how conversational state (memory) is passed between nodes
- To build an interactive chatbot that maintains context across user turns

Architecture:
The chatbot is implemented as a simple directed graph with the following nodes:

    User Input → Memory → LLM → Output → END

- User Input Node:
  Receives the latest user message.

- Memory Node:
  Appends user and assistant messages to a conversation history stored in state.

- LLM Node:
  Uses a mocked language model (FakeLLM) to generate context-aware but
  non-factual responses based on conversation history.

- Output Node:
  Prints the assistant response to the terminal.

State Management:
- The ChatState object explicitly stores:
  - user_input: latest user message
  - memory: list of past conversation turns
  - response: latest assistant reply

LLM Design Choice:
- A mock LLM is used instead of a real API-based model.
- This keeps the chatbot fully offline and dependency-free.
- The focus is on graph structure, state flow, and memory—not model quality.

Behavior:
- The chatbot runs interactively in the terminal.
- It maintains conversational context across turns.
- It does not extract or recall factual details (e.g., names), by design.

This implementation is intentionally minimal and learning-focused, to understand langgraph fundamentals.
"""


from typing import TypedDict, List
from langgraph.graph import StateGraph, END

class FakeLLM:
    """
    Simple mock LLM that produces natural, memory-aware
    but non-factual responses.
    """

    def invoke(self, conversation: str) -> str:
        text = conversation.lower()

        if "what's my name" in text or "do you know my name" in text:
            return "I remember our conversation, but I can’t recall specific personal details."

        if len(conversation.splitlines()) > 4:
            return "I’m following along and remember what we’ve talked about so far."

        return "Okay, tell me more."


# Graph State

class ChatState(TypedDict):
    user_input: str
    memory: List[str]
    response: str



# Nodes


def user_input_node(state: ChatState) -> ChatState:
    return state


def memory_node(state: ChatState) -> ChatState:
    state["memory"].append(f"User: {state['user_input']}")
    return state


def llm_node(state: ChatState) -> ChatState:
    llm = FakeLLM()

    conversation = "\n".join(state["memory"])
    response = llm.invoke(conversation)

    state["response"] = response
    state["memory"].append(f"Assistant: {response}")

    return state


def output_node(state: ChatState) -> ChatState:
    print(f"Assistant: {state['response']}")
    return state


# Build Graph

def build_chatbot():
    graph = StateGraph(ChatState)

    graph.add_node("user_input", user_input_node)
    graph.add_node("memory", memory_node)
    graph.add_node("llm", llm_node)
    graph.add_node("output", output_node)

    graph.set_entry_point("user_input")

    graph.add_edge("user_input", "memory")
    graph.add_edge("memory", "llm")
    graph.add_edge("llm", "output")
    graph.add_edge("output", END)

    return graph.compile()


# Interactive Terminal Loop


if __name__ == "__main__":
    app = build_chatbot()

    state: ChatState = {
        "user_input": "",
        "memory": [],
        "response": "",
    }

    print("Simple Chatbot started. Type 'exit' to quit.\n")

    while True:
        user_text = input("User: ").strip()

        if user_text.lower() in {"exit", "quit"}:
            print("Chat ended.")
            break

        state["user_input"] = user_text
        state = app.invoke(state)
