FROM python:3.12

COPY ./ /app-python/

COPY requirements.txt /app-python/requirements.txt

WORKDIR /app-python/src

RUN pip install --no-cache-dir -r /app-python/requirements.txt

EXPOSE 2113

ENTRYPOINT ["python3.12", "main.py"]