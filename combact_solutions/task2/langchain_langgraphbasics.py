'''
LangChain & LangGraph Basics Demo (mocked LLM)

This module demonstrates the fundamental building blocks of LangChain and LangGraph
using a mocked Large Language Model (LLM) to avoid external API dependencies.

What this demo covers:
- Prompt templating using PromptTemplate
- Manual conversational memory handling
- Separation of prompt, model, and state
- A minimal LangGraph execution flow (Input -> LLM -> Output)

Why a mocked LLM ?:
- API access and billing may not be available 
- The focus is on understanding architecture and data flow, not model quality
- Enables deterministic, offline, and reproducible demos

Components:
1) FakeLLM: Simulates an LLM interface with an invoke() method
2) LangChain demo: Shows prompt formatting and conversation history injection
3) LangGraph demo: Shows graph-based orchestration using a single LLM node

Note:
This code is intentionally minimal and educational. It is not intended for production use.

'''


from typing import TypedDict, List
from langchain_core.prompts import PromptTemplate
from langgraph.graph import StateGraph, END



# mocking  LLM (no API, no billing)


class FakeResponse:
    def __init__(self, content: str):
        self.content = content


class FakeLLM:
    
    #mocked LLM used for demos when API access or billing is unavailable.
    

    def invoke(self, prompt: str) -> FakeResponse:
        return FakeResponse(
            content=f"[MOCK LLM RESPONSE]\nPrompt received:\n{prompt[:200]}..."
        )


# langChain basics (concept demo)


def run_langchain_demo() -> None:
    prompt = PromptTemplate(
        input_variables=["history", "user_input"],
        template="""
you are a helpful assistant.

conversation so far:
{history}

User: {user_input}
Assistant:
""",
    )

    llm = FakeLLM()
    history: List[str] = []

    def run_turn(user_input: str) -> str:
        formatted_prompt = prompt.format(
            history="\n".join(history),
            user_input=user_input,
        )

        response = llm.invoke(formatted_prompt).content

        history.append(f"User: {user_input}")
        history.append(f"Assistant: {response}")

        return response

    print("\nLangChain Demo (Mocked) ")
    print(run_turn("What is LangChain?"))
    print(run_turn("Why is memory useful?"))



# langGraph basics

class GraphState(TypedDict):
    user_input: str
    output: str


def llm_node(state: GraphState) -> GraphState:
    llm = FakeLLM()
    response = llm.invoke(state["user_input"]).content

    return {
        "user_input": state["user_input"],
        "output": response,
    }


def run_langgraph_demo() -> None:
    graph = StateGraph(GraphState)

    graph.add_node("llm", llm_node)
    graph.set_entry_point("llm")
    graph.add_edge("llm", END)

    app = graph.compile()

    print("\nLangGraph Demo (Mocked)")
    result = app.invoke(
        {"user_input": "Explain LangGraph in one sentence."}
    )
    print(result["output"])



# Main


if __name__ == "__main__":
    run_langchain_demo()
    run_langgraph_demo()
