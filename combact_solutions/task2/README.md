# LangChain & LangGraph Basics (Simple Demo)

## What is this project?
This project is a **small demo** to learn the basics of **LangChain** and **LangGraph**.

It shows how:
- A prompt is created
- An LLM (model) is called
- Input goes in and output comes out
- LangGraph runs logic as a graph

The LLM is **mocked**, so no API key or billing is needed.



## Why I made this
I had **no previous experience** with LangChain or LangGraph.  
The task requirements were not very detailed, so I learned by **trying things out and experimenting**.

This helped me understand:
- How prompts work
- How data flows through the system
- How LangGraph is different from normal scripts



## What does “vibe coded” mean here?
Some parts were **vibe coded**, meaning:
- I started simple instead of planning everything first
- I experimented to see what works
- I fixed things as I learned more about the libraries

This was intentional because these libraries are new and change fast.  
The final code is simple but done with understanding.



## Why the LLM is mocked
Instead of using a real LLM API, I used a **FakeLLM** because:
- API keys or billing may not be available
- The goal is learning structure, not model answers
- The demo should run offline without errors

This is common practice in learning and early development.



## What this demo shows

### LangChain
- Prompt creation using `PromptTemplate`
- Simple conversation memory using history
- Clear flow: prompt → model → response

### LangGraph
- Logic written as a graph
- One node that processes input
- Flow: Input → LLM → Output
    

## Limitations
- No real AI responses
- Only one LangGraph node
- No data saved between runs

These limits are fine for a beginner demo.



## Final note
This project focuses on **learning and understanding**, not production use.  
through this I understood the **basic ideas** behind LangChain and LangGraph in a simple and clear way.
