import logging
from datetime import datetime
from libs.pubsub import PubSub
from models.settings import Settings


def process_event(event, pubsub):
    """
    This is a callback that gets passed to the `PubSub.subscribe()` method.
    When no events are received within a certain time period, the API's subscribe
    method sends keepalive messages and the latest replay ID through this callback.
    """
    if event.events:
        print("Number of events received in FetchResponse: ", len(event.events))
        # If all requested events are delivered, release the semaphore
        # so that a new FetchRequest gets sent by `PubSub.fetch_req_stream()`.
        if event.pending_num_requested == 0:
            pubsub.release_subscription_semaphore()

        for evt in event.events:
            # Get the event payload and schema, then decode the payload
            payload_bytes = evt.event.payload
            json_schema = pubsub.get_schema_json(evt.event.schema_id)
            decoded_event = pubsub.decode(json_schema, payload_bytes)
            print("Payload", payload_bytes)
            print("Decoded", decoded_event)
    else:
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] The subscription is active.")

    # The replay_id is used to resubscribe after this position in the stream if the client disconnects.
    # Implement storage of replay for resubscribe!!!
    event.latest_replay_id


def run(settings: Settings) -> None:
    sfdc_updater = PubSub(settings)
    sfdc_updater.auth()
    sfdc_updater.publish(settings.TOPIC)
    sfdc_updater.subscribe(settings.TOPIC, "LATEST", "", 1, process_event)


if __name__ == "__main__":
    settings = Settings()
    logging.basicConfig(level=logging.DEBUG if settings.DEBUG else logging.INFO)
    logging.debug(settings)
    run(settings)
