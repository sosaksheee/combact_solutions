# LLM Endpoint Load & Latency Tester

## Project Overview

This project is a **lightweight load and latency testing tool** for Large Language Model (LLM) endpoints.

It is designed to help developers and interns **measure performance characteristics** such as latency, throughput, and request-level metrics for LLM APIs.

The tool supports **two execution modes**:

* **Real mode** – calls an actual LLM endpoint using environment variables
* **Mock mode** – simulates LLM latency locally without any network calls

---

## Objective

* Understand LLM performance metrics (latency, throughput)
* Test endpoint responsiveness under sequential load
* Generate structured metrics for analysis
* Enable safe local testing without API costs

---

## What This Tool Does

* Sends multiple prompts to an LLM endpoint (or mock simulator)
* Measures end-to-end request latency
* Logs per-request metrics to CSV
* Generates a summary report in JSON
* Supports reproducible testing with timestamps and run IDs

---

## Modes of Operation

### 1. Real Mode

* Calls a real LLM API endpoint
* Requires environment variables for configuration
* Measures actual network + model latency

### 2. Mock Mode (`--mock`)

* Simulates realistic LLM response times
* No internet or API keys required
* Useful for development, testing, and CI pipelines

---

## Metrics Generated

### Per-request Metrics (`metrics_requests.csv`)

* Run ID
* Prompt ID
* Prompt text
* Latency (seconds)
* Timestamp (UTC)
* Mode (mock / real)

### Summary Metrics (`metrics_summary.json`)

* Total requests
* Total execution time
* Average latency
* Minimum latency
* Maximum latency
* Throughput (requests per second)

---

## Project Structure

```
.
├── test_endpoint.py
├── metrics_requests.csv
├── metrics_summary.json
└── README.md
```

---

## Prerequisites

* Python 3.9+
* `requests` library

Install dependencies:

```bash
pip install requests
```

---

## Environment Variables (Real Mode Only)

Set the following variables before running in real mode:

```bash
export LLM_ENDPOINT_URL="<your-endpoint-url>"
export LLM_API_KEY="<your-api-key>"
export LLM_MODEL_NAME="<model-name>"
```

---

## How to Run

### Run in Mock Mode (Recommended for Testing)

```bash
python test_endpoint.py --mock
```

### Run in Real Mode

```bash
python test_endpoint.py
```

---

## Sample Output

```
[1] Latency: 0.842s
[2] Latency: 0.611s
[3] Latency: 1.032s

--- summary ---
average_latency_seconds: 0.8281
throughput_rps: 1.21
```

Metrics files are written to:

* `metrics_requests.csv`
* `metrics_summary.json`

---

## Design Notes

* Uses `time.perf_counter()` for accurate latency measurement
* Mock mode preserves the same metrics pipeline as real mode
* Sequential request testing provides clear latency insights
* Focuses on **observability**, not concurrency

---

## Use Cases

* LLM API benchmarking
* MLOps experimentation
* Latency vs throughput analysis
* CI-safe performance testing

---

