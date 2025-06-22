# DockerHub Statistics Exporter

This project provides a lightweight exporter that retrieves DockerHub repository statistics and makes them available for monitoring systems such as Prometheus.

## Overview

The application queries DockerHub for repository data—like pull counts and stars—and exposes them via an HTTP endpoint. It is containerized via Docker and can be deployed to Kubernetes using the provided manifests.

## 📁 Project Structure

```
.
├── README.md                # Top-level README (this file)
├── app-python/              # Python-based exporter application
│   ├── Dockerfile           # Docker image definition for the app
│   ├── Makefile             # Common commands for building/running
│   ├── README.md            # App-specific documentation
│   ├── requirements.txt     # Python dependencies
│   └── src/
│       ├── __init__.py
│       └── main.py          # Application entry point
└── k8s-resources/           # Kubernetes manifests
    ├── app.yml              # Deployment & Service definitions
    └── utils.yml            # (Optional) Supporting resources
```

## Getting Started

### Prerequisites

* Python 3.8+
* Docker
* Kubernetes cluster (e.g. minikube, kind)
* `kubectl` installed

### Build & Run Locally

```bash
cd app-python
make install     # Install dependencies
make run         # Run the app locally
```

### Build Docker Image

```bash
make docker-build
```

### Run with Docker

```bash
make docker-run
```

## Kubernetes Deployment

To deploy the app on Kubernetes:

```bash
kubectl apply -f k8s-resources/app.yml
```

To verify the deployment:

```bash
kubectl get pods
kubectl port-forward svc/dockerhub-stats-exporter 8080:80
```

Then visit `http://localhost:8080/metrics` to view the exposed stats.

## Exported Metrics

Once deployed, the service exposes metrics in Prometheus format at `/metrics`. Example metrics:

```
dockerhub_repository_pull_count{repository="user/image"} 12345
dockerhub_repository_star_count{repository="user/image"} 67
```

## Subdirectories

### `app-python/`

Contains the Python application that fetches and exposes DockerHub stats. See its [README](./app-python/README.md) for development details.

### `k8s-resources/`

Includes all the Kubernetes manifests:

* `app.yml`: Core Deployment and Service configuration
* `utils.yml`: Additional resources like ConfigMaps or RBAC (if any)


