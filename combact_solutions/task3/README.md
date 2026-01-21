# Simple Interactive Chatbot with Memory (LangGraph)

## Overview
This project is a **simple interactive chatbot** built using **LangGraph concepts**.
The chatbot runs in the terminal, accepts user input, stores conversation history, and responds in a natural way.

The focus of this project is to understand **how conversational memory and state work in a graph-based system**, not to build a fully intelligent assistant.

A mocked LLM is used so the chatbot runs without API keys or billing.



## Why This Project Was Built
This task was done as a learning exercise with **new libraries and concepts**.

I had **no prior experience with LangGraph**, especially with:
- Graph state
- Node-based execution
- Managing conversational memory explicitly

Because of this, parts of the **graph state and node structure were vibe coded** — meaning I experimented, observed behavior, and adjusted the structure to understand how memory flows through the chatbot.

This approach helped me quickly learn how:
- State is passed between nodes
- Memory persists across turns
- A chatbot can feel conversational without complex logic


## What “Vibe Coding” Means Here
When I say I *vibe coded* the graph state and nodes, it means:
- I didn’t design everything perfectly upfront
- I experimented with node order and state fields
- I learned by running the chatbot and seeing how memory behaved

This was intentional because **graph-based conversational memory was new to me**, and experimentation helped me understand it faster than only reading documentation.

The final structure is simple but intentional.

## Chatbot Behavior

### What the chatbot does
- Takes user input from the terminal
- Stores conversation history (context memory)
- Uses past messages to influence responses
- Responds interactively until the user exits
- Uses a graph (not a linear script)

### What the chatbot does NOT do
- It does **not** store personal facts (like names)
- It does **not** recall specific user details
- It does **not** answer fact-based memory questions

This behavior is **by design**.


## Conversational Memory vs Fact Memory

### Conversational Memory (Implemented)
- Stores previous messages
- Makes the chatbot aware of context
- Helps responses feel continuous and natural

### Fact Memory (Not Implemented)
- No name storage
- No personal detail recall
- No structured data extraction

Fact memory was **intentionally excluded** to keep the chatbot simple and focused on learning conversational state.


## Architecture Overview

### Nodes Used
1. **User Input Node** – receives user message
2. **Memory Node** – stores conversation history
3. **LLM Node (Mocked)** – generates a response using memory
4. **Output Node** – prints the response

### Graph Flow
User Input → Memory → LLM → Output

## Why the LLM Is Mocked
A mock LLM is used because:
- API access or billing may not be available
- The goal is architecture and learning
- The chatbot should run offline
- Model quality is not the focus

## Limitations
- No real LLM
- No fact memory
- No long-term storage
- No advanced reasoning

## Conclusion
This project demonstrates:
- Basic chatbot construction
- Explicit state management
- Conversational memory using LangGraph