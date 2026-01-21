#  MLOps for LLMs: Endpoint Testing & Observability

## Overview
This project implements a lightweight MLOps-style testing script for a deployed Large Language Model (LLM) endpoint.  
The goal is to simulate real production usage by measuring **latency** and **throughput**, and by logging metrics for later analysis.

The script supports both:
- **Real mode** – calls an actual deployed LLM endpoint
- **Mock mode** – simulates LLM latency when cloud access or credentials are unavailable



## Features
- Calls an LLM endpoint using HTTP requests
- Measures per-request latency
- Computes throughput (requests per second)
- Tests multiple prompts for consistency
- Logs metrics to:
  - `metrics_requests.csv` (per-request)
  - `metrics_summary.json` (run-level summary)
- Secure configuration via environment variables
- Mock mode for offline/local testing



## Requirements
- Python 3.9+
- `requests` library

Install dependencies:
```bash
pip install requests

