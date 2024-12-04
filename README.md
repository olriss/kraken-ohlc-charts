# Kraken OHLC Prometheus Exporter

This project demonstrates the process of creating a Prometheus exporter to fetch OHLC (Open, High, Low, Close) data from the **Kraken Exchange Public API** and visualizing it in Grafana.

## Overview

1. The Prometheus exporter connects to the **Kraken Public API** to retrieve OHLC data for selected cryptocurrency trading pairs.
2. The data is exposed in a Prometheus-compatible format using the `prometheus_client` library.
3. Prometheus scrapes this data at regular intervals.
4. The data is visualized in **Grafana** dashboards with custom metrics and alerts.

---

## Features

- Fetches OHLC data for multiple trading pairs from Kraken's Public API.
- Includes additional metrics such as **VWAP (Volume Weighted Average Price)** and **trading volume**.
- Exposes the data using Prometheus-compatible metrics.
- Packaged as a **Docker container** for deployment in Kubernetes (K3s).
- Ingress and service configuration for Grafana dashboards.

---

## Workflow

### 1. Prometheus Exporter
The exporter is written in Python and uses the following libraries:
- `prometheus_client` for exposing metrics.
- `requests` for fetching data from Kraken's Public API.

### Example Prometheus Metrics:
- `kraken_ohlc_open{pair="BTCUSD"}`
- `kraken_ohlc_high{pair="BTCUSD"}`
- `kraken_ohlc_low{pair="BTCUSD"}`
- `kraken_ohlc_close{pair="BTCUSD"}`
- `kraken_ohlc_vwap{pair="BTCUSD"}`
- `kraken_ohlc_volume{pair="BTCUSD"}`

Metrics are updated every 5 minutes, while the data retrieved from Kraken API has an interval of 1 hour.

---

### 2. Dockerization
The Python application is containerized using Docker. The `Dockerfile` includes the following steps:
- Base image: Python 3.x
- Dependencies are installed in a virtual environment.
- The Prometheus exporter is launched on port `8000`.

#### Example Docker Commands:
```bash
docker build -t ohlc-exporter:latest .
docker save -o ohlc-exporter.tar ohlc-exporter:latest
