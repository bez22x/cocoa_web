FROM python:3.9-slim
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run_model.py .
CMD [ "python", "run_model.py" ]