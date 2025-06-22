import os
import requests
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, Response

app = Flask(__name__)

docker_image_pulls = Gauge('docker_image_pulls', 'The total number of Docker image pulls', ['name', 'organization'])
DOCKERHUB_ORGANIZATION = str(os.getenv("DOCKERHUB_ORGANIZATION"))

@app.route('/')
def main():
    return "Docker image pulls metric exporter is running."

@app.route('/metrics', methods=["GET"])
def get_img_pulls():
    try:
        resp = requests.get(f"https://hub.docker.com/v2/repositories/{DOCKERHUB_ORGANIZATION}/?page_size=25&page=1")
        resp.raise_for_status()  # Raise an exception for HTTP errors (status codes >= 400)
        resp_json = resp.json()

        for image in resp_json['results']:
            name = image['name']
            pulls = format(image['pull_count'], ".6e")

            docker_image_pulls.labels(name=name, organization=DOCKERHUB_ORGANIZATION).set(pulls)

        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
    except requests.exceptions.RequestException as ex:
        return str(ex), 500  # Return the error message with HTTP status code 500

if __name__ == '__main__':
    app.run(port=2113, debug=True)
