FROM python:3.9-slim
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./flask_cocoa ./flask_cocoa
COPY server.py .
CMD [ "python", "server.py" ]