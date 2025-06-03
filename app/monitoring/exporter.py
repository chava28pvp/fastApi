# monitoring/exporter.py

from prometheus_client import start_http_server, Gauge
import requests, time, threading

API_ENDPOINTS = [
     {"name": "roles", "url": "http://localhost:8000/roles/"},
    {"name": "users", "url": "http://localhost:8000/users/"},
]

api_up = Gauge('api_up', 'API status (1=up, 0=down)', ['name'])
api_response_time = Gauge('api_response_time_seconds', 'API response time in seconds', ['name'])

def monitor_loop():
    while True:
        for api in API_ENDPOINTS:
            try:
                start = time.time()
                response = requests.get(api["url"], timeout=3)
                latency = time.time() - start
                api_up.labels(name=api["name"]).set(1 if response.ok else 0)
                api_response_time.labels(name=api["name"]).set(latency)
            except Exception:
                api_up.labels(name=api["name"]).set(0)
                api_response_time.labels(name=api["name"]).set(-1)
        time.sleep(10)

def start_monitoring():
    start_http_server(9100)
    threading.Thread(target=monitor_loop, daemon=True).start()
