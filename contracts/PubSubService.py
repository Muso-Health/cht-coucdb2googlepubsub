from abc import ABC


class PubSubService(ABC):
    def dispatch_to_pub_sub(self, topic: str, json_dict: dict) -> str:
        pass

    def get_topic_from_data(self, json_dict: dict) -> str:
        pass

    def get_task_topic(self, json_dict: dict) -> str:
        pass
