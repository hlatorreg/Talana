FROM python:3.10.0-slim

WORKDIR /talana

COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -e .[dev]

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
EXPOSE 5000/tcp