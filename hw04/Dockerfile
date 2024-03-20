FROM python:3.10.5-slim

RUN apt-get update && apt-get install -y curl git

WORKDIR /hw04/

COPY requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["bash"]
CMD ["-c", "uvicorn app.main:app --host 0.0.0.0 --port 8020"]