import grpc
import location_pb2
import location_pb2_grpc
import logging

# Run this code to make sample request

logging.basicConfig(
    handlers=[logging.StreamHandler()], format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
    level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")

logging.info("Starting...")

try:
    channel = grpc.insecure_channel("localhost:5005")
    logging.info("Connected to localhost:5005")
    stub = location_pb2_grpc.LocationServiceStub(channel)

    # Update with your payload
    order = location_pb2.LocationMessage(
        id=10001,
        person_id=5,
        longitude='18.0',
        latitude='3.0',
        creation_time="2022-07-29T11:29:01"
    )
    response = stub.Create(order)
    logging.info(format(response))

except Exception as e:
    print(e)
    logging.error("Error occurs")
