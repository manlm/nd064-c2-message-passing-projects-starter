import json
from kafka import KafkaProducer
import time
import logging

from concurrent import futures

import grpc
import location_pb2_grpc
import location_pb2

producer = None
try:
    KAFKA_SERVER = 'localhost:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
except:
    KAFKA_SERVER = 'kafka-headless:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        global producer
        logging.info("Create location start")

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        logging.info("new location: " + json.dumps(request_value))
        data = json.dumps(request_value).encode()

        logging.info("Send message to kafka")
        TOPIC_NAME = 'location'
        producer.send(TOPIC_NAME, data)
        producer.flush()

        logging.info("Create location end")
        return location_pb2.LocationMessage(**request_value)


def serve():
    logging.basicConfig(
        handlers=[logging.StreamHandler()], format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
        level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")

    logging.info("Initialize gRPC server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
    logging.info("Location gRPC server initialized")

    logging.info("Server starting on port 5005...")
    server.add_insecure_port("[::]:5005")
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
