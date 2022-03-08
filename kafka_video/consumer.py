from flask import Flask, Response
from kafka import KafkaConsumer
import os

kafka_port = int(os.environ['KAFKA_PORT'])
kafka_host = os.environ["KAFKA_HOST"]
consumer = KafkaConsumer(
    os.environ['KAFKA_TOPIC'],
    bootstrap_servers=f'{kafka_host}:{kafka_port}',
    group_id='my-group',
    api_version=(2, 8, 1))

app = Flask(__name__)


def kafkastream():
    for message in consumer:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + message.value + b'\r\n\r\n')


@app.route('/')
def index():
    return Response(kafkastream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
