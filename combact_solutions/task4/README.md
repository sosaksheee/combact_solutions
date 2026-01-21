# Docker Basics – Containerized Chatbot

## Project Overview

This project demonstrates **Docker Basics** by containerizing a simple terminal-based chatbot written in Python.

The chatbot uses:

* A graph-based workflow
* Memory handling
* A mock LLM (FakeLLM)

Docker is used to package the chatbot so it can run **anywhere without environment issues**.

---

## Objective

* Learn Docker fundamentals
* Containerize a Python application
* Build and run a Docker image locally
* Eliminate "works on my machine" problems

---

## What the Chatbot Does

* Accepts user input from the terminal
* Stores conversation history
* Generates simple, memory-aware responses
* Runs continuously until the user exits

---

## Why Docker is Used

Docker allows:

* Portability across systems
* Consistent runtime environment
* Easy deployment
* No need to install Python or libraries manually

---

## Project Structure

```
.
├── chatbot.py
├── Dockerfile
└── README.md
```

---

## Prerequisites

Make sure the following is installed:

* **Docker Desktop**

  * Windows / Mac / Linux
  * Download: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

---

## Step 1: Build Docker Image

Run this command from the project directory:

```bash
docker build -t chatbot-app .
```

### Command Breakdown

* `docker build` → Builds a Docker image
* `-t chatbot-app` → Names the image
* `.` → Uses the current directory containing the Dockerfile

---

## Step 2: Run Docker Container

```bash
docker run -it chatbot-app
```

### Command Breakdown

* `docker run` → Starts a container
* `-it` → Interactive terminal mode
* `chatbot-app` → Image name

---

## Sample Output

```
Simple Chatbot started. Type 'exit' to quit.

User: Hello
Assistant: Okay, tell me more.

User: Do you remember me?
Assistant: I’m following along and remember what we’ve talked about so far.

Type exit to stop the chatbot.
```

---

## Notes

* This project is intended for learning Docker basics.
* The chatbot logic is intentionally simple to keep the focus on containerization.
* The same Docker image can run on any system with Docker installed.
