# Salesforce Pub/Sub API Python Client

This Python class provides helpers to use the Salesforce Pub/Sub API, allowing you to subscribe to and publish Platform Events.

https://developer.salesforce.com/docs/platform/pub-sub-api/overview

## Prerequisites

- Python 3.x
- Salesforce organization with Pub/Sub API enabled
- Avro library (`pip install avro`)
- gRPC library (`pip install grpcio`)

## Installation

```
pip install pysfpubsub
```

### Usage

```
from datetime import datetime
from pysfpubsub import Client

def callback(event, client):
    """
    This is a callback that gets passed to the `Client.subscribe()` method.
    When no events are received within a certain time period, the API's subscribe
    method sends keepalive messages and the latest replay ID through this callback.
    """
    if event.events:
        print("Number of events received in FetchResponse: ", len(event.events))
        # If all requested events are delivered, release the semaphore
        # so that a new FetchRequest gets sent by `Client.fetch_req_stream()`.
        if event.pending_num_requested == 0:
            client.release_subscription_semaphore()

        for evt in event.events:
            # Get the event payload and schema, then decode the payload
            payload_bytes = evt.event.payload
            json_schema = client.get_schema_json(evt.event.schema_id)
            decoded_event = client.decode(json_schema, payload_bytes)
            print(decoded_event)
    else:
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] The subscription is active.")

sfdc_handler = Client(
    url="https://login.salesforce.com",
    username="your_username",
    password="your_password",
    grpc_host="api.pubsub.salesforce.com",
    grpc_port=7443,
    api_version="57.0"
)
sfdc_handler.auth()
sfdc_handler.subscribe(
    topic="/event/Event_Example__c",
    replay_type="LATEST",
    replay_id=None,
    num_requested=10,
    callback=callback
)
```