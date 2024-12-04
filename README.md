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