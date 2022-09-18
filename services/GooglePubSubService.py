import json
import time
from datetime import datetime

from google.cloud import pubsub_v1

from contracts.PubSubService import PubSubService
from models.config.Config import Config


class GooglePubSubService(PubSubService):
    publisher = None

    def dispatch_to_pub_sub(self, topic: str, json_dict: dict) -> str:
        if self.publisher is None:
            self.publisher = pubsub_v1.PublisherClient()

        topic_path = self.publisher.topic_path('muso-health-cdi', topic)
        data_str = json.dumps(json_dict)
        data = data_str.encode("utf-8")
        future = self.publisher.publish(topic_path, data)
        message_id = future.result()
        return message_id

    def get_topic_from_data(self, json_dict: dict) -> str:
        try:
            reported = datetime.fromtimestamp(json_dict['reported_date']/1000.0)
            year = reported.year
            current_year = datetime.now().year
            if Config.old_accepted:
                if year > current_year:
                    return ''
                if year < 2017:
                    return 'mali-prod-data-records-2016'
                return f"mali-prod-data-records-{year}"
            elif round(time.time() * 1000) - json_dict['reported_date'] < 6 * 30 * 24 * 3600 * 1000:
                return f"mali-prod-data-records-{year}"
            else:
                return ''

        except:
            return ''


