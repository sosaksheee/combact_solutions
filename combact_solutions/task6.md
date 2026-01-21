# Simple Prompt Engineering

## Objective
The goal of this task is to experiment with different prompt designs and observe how a GPT-style model responds to changes in prompt clarity, structure, and constraints.

This task treats **prompts as a design tool**, not just user input.



## Setup
The same underlying question was asked using different prompt variations in the shared chat:

> Explain LangGraph in simple terms.

Each prompt was evaluated based on:
- Clarity of the response
- Structure and organization
- Relevance to the question
- Hallucination risk
- Ease of understanding for a beginner


## Prompt Variations and Observations

### Prompt 1: Open-Ended Prompt
Explain LangGraph.

**Observed Model Behavior:**
- Response was broad and generic
- Assumed technical background
- Lacked examples or structure
- Contained abstract descriptions

**Analysis:**
Because the prompt was vague, the model had to guess the expected depth and audience, which resulted in a less focused answer.

**Verdict:**  Weak prompt



### Prompt 2: Role-Based Prompt
You are a helpful AI assistant.
Explain LangGraph in simple terms.

**Observed Model Behavior:**
- Tone was friendlier and more conversational
- Explanation was clearer than Prompt 1
- Still somewhat technical
- Structure was improved but not guaranteed

**Analysis:**
Adding a role improved tone and intent, but the model still lacked guidance on format and level of detail.

**Verdict:**  Moderate improvement



### Prompt 3: Structured and Constrained Prompt
You are a helpful AI assistant.
Explain LangGraph in simple terms using:

One short paragraph

No technical jargon

A simple example

**Observed Model Behavior:**
- Clear and concise explanation
- Beginner-friendly language
- Included a simple, relevant example
- Minimal unnecessary details
- Lower hallucination risk

**Analysis:**
Explicit constraints helped the model focus on clarity and relevance. The structure reduced ambiguity and guided the model toward the desired output.

**Verdict:**  Best-performing prompt



## Best Prompt and Reasoning

**Prompt 3 worked best.**

Reasons:
- Clear constraints reduced ambiguity
- Structured format guided the model’s response
- Simpler language reduced hallucinations
- Example grounded the explanation in reality

This shows that **prompt structure directly influences model behavior and output quality**.



## Key Learnings
- Prompts are a form of interface design
- More constraints often lead to better outputs
- Role + structure improves clarity
- Prompt engineering is an iterative process


## Reference Chat

The prompt engineering experiments and observations were based on the following ChatGPT conversation:

[ChatGPT Conversation Link](https://chatgpt.com/share/697077da-83b4-8007-ae07-57b0a5974910)


## Conclusion
This task demonstrated that small changes in prompt wording and structure can significantly affect LLM responses. Treating prompts as a design tool enables better control over clarity, structure, and reliability of model outputs.
