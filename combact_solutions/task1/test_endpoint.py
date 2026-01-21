"""
LLM Endpoint Load & Latency Tester (with --mock mode)

Modes:
1.Real mode: calls an actual LLM endpoint (requires env vars)
2.Mock mode: simulates LLM latency for local testing

Outputs:
*metrics_requests.csv
*metrics_summary.json

"""

import os
import time
import json
import csv
import argparse #parse the --mock command-line flag
import random
import statistics
import requests
from datetime import datetime, timezone
from typing import List, Dict #improve code readability and type safety


REQUESTS_CSV = "metrics_requests.csv"
SUMMARY_JSON = "metrics_summary.json"


def load_config() -> dict:
    #load LLM configuration from environment variables.
    config = {
        "endpoint": os.getenv("LLM_ENDPOINT_URL"),
        "api_key": os.getenv("LLM_API_KEY"),
        "model": os.getenv("LLM_MODEL_NAME"),
    }

    missing = [k for k, v in config.items() if not v]
    if missing:
        raise EnvironmentError(f"Missing environment variables: {missing}")

    return config


def call_llm(endpoint: str, api_key: str, model: str, prompt: str) -> float:
    #call a real LLM endpoint and return request latency.
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }

    start = time.perf_counter() # perf_counter is used for accurate end-to-end latency measurement
    response = requests.post(endpoint, headers=headers, json=payload, timeout=30)
    end = time.perf_counter()

    response.raise_for_status()
    return end - start


def mock_llm_call(min_delay: float = 0.3, max_delay: float = 1.2) -> float:
    #simulate LLM latency without any network calls.
    latency = random.uniform(min_delay, max_delay)
    time.sleep(latency)
    return latency


def write_csv(rows: List[Dict]) -> None:
    #write per-request metrics to CSV.
    with open(REQUESTS_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def write_json(summary: Dict) -> None:
    #write run-level metrics to JSON.
    with open(SUMMARY_JSON, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)


def run_tests(prompts: List[str], mock_mode: bool) -> None:
    latencies: List[float] = []
    request_logs: List[Dict] = []
    run_id = datetime.now(timezone.utc).isoformat()

# configuration is only loaded in real mode to keep mock execution self-contained
    config = None
    if not mock_mode:
        config = load_config()

    print("\n--- running LLM endpoint tests ---")
    print(f"Mode: {'MOCK' if mock_mode else 'REAL'}\n")

    overall_start = time.perf_counter()

    for idx, prompt in enumerate(prompts, start=1):
         # mock mode avoids network calls while preserving the same metrics pipeline
        if mock_mode: 
            latency = mock_llm_call()
        else:
            latency = call_llm(
                config["endpoint"],
                config["api_key"],
                config["model"],
                prompt,
            )

        latencies.append(latency)

        request_logs.append({
            "run_id": run_id,
            "prompt_id": idx,
            "prompt": prompt,
            "latency_seconds": round(latency, 4),
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "mode": "mock" if mock_mode else "real",
        })

        print(f"[{idx}] Latency: {latency:.3f}s")

    total_time = time.perf_counter() - overall_start
    throughput = len(prompts) / total_time # throughput captures system capacity under sequential load (requests per sec)

    summary = {
        "run_id": run_id,
        "mode": "mock" if mock_mode else "real",
        "total_requests": len(prompts),
        "total_time_seconds": round(total_time, 3),
        "average_latency_seconds": round(statistics.mean(latencies), 4),
        "min_latency_seconds": round(min(latencies), 4),
        "max_latency_seconds": round(max(latencies), 4),
        "throughput_rps": round(throughput, 2),
    }

    write_csv(request_logs)
    write_json(summary)

    print("\n--- summary ---")
    for k, v in summary.items():
        print(f"{k}: {v}")

    print("\nmetrics written to:")
    print(f"- {REQUESTS_CSV}")
    print(f"- {SUMMARY_JSON}")


def parse_args():
    parser = argparse.ArgumentParser(description="LLM Endpoint Tester")
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Run in mock mode without calling a real LLM endpoint",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    test_prompts = [
        "explain MLOps in simple terms.",
        "what are challenges in deploying LLMs?",
        "explain latency vs throughput.",
        "give an example of prompt inconsistency.",
    ]

    print(f"mock_mode={args.mock}") #verifies execution mode during evaluation

    run_tests(test_prompts, mock_mode=args.mock)
