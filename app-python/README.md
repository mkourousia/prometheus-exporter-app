# Docker Image Pulls Metric Exporter

This Flask application serves Prometheus metrics for Docker image pulls from Docker Hub.

## Configuration

1. Flask Application Setup: The code imports necessary modules (os, requests, Flask) and initializes a Flask application.

2. Environment Variable Configuration: It retrieves the value of the DOCKERHUB_ORGANIZATION environment variable. This variable is expected to contain the name of the Docker Hub organization whose image pulls metrics will be monitored.

3. Route Definitions:
    The / route simply returns a message indicating that the Docker image pulls metric exporter is running.
    The /metrics route handles requests for Prometheus metrics. It queries the Docker Hub API to retrieve pull counts for images belonging to the specified organization.

4. Docker Hub API Request: The code sends a GET request to the Docker Hub API to retrieve information about repositories belonging to the specified organization.

5. Parsing API Response: If the request is successful (status code 200), the response JSON is parsed to extract the image names and their corresponding pull counts.

6. Prometheus Metrics Format: The code formats the retrieved data into Prometheus-compatible metrics format. It defines a gauge type metric named docker_image_pulls, including labels for image name and organization.

7. Returning Metrics: The formatted metrics are returned as the response to /metrics requests.


## Dependencies

1. Create a python virtual environment

```
python3 -m venv ./test
source test/bin/activate
```

2. Install dependencies

```
pip install -r requirements.txt
```

## Usage

1. Set up environment variable:

- `DOCKERHUB_ORGANIZATION`: Docker Hub organization name.

2. Run the Flask application

```
python src/main.py
```

3. Access metrics

- Open a web browser and go to http://localhost:2113/metrics to view Prometheus metrics.


## Docker Support

This application can also be containerized using Docker. A Dockerfile is provided in the repository.

```
docker build -t docker-image-pulls-metric-exporter .
docker run -p 2113:2113 -e DOCKERHUB_ORGANIZATION=<organization_name> docker-image-pulls-metric-exporter
```

## Deploy on Kubernetes

To deploy the app named "maria-app" with the specified requirements apply the manifest files under k8s-resources. 

```
kubectl apply -f k8s-resources/
```

This will create a deployment and a service that listens on metric port 2113 in the "default" namespace. The required environment variable's value must be set in the deployment's manifest.

```
        env:
        - name: DOCKERHUB_ORGANIZATION
          value: camunda
```