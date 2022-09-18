from datetime import datetime


class BatchInfo:
    def __init__(self,
                 batch_id: int,
                 start_at: datetime,
                 pending: int,
                 end_at: datetime = None,
                 received: int = 0,
                 received_forms: int = 0,
                 validated_forms: int = 0,
                 malformed_forms: int = 0,
                 flatten_forms: int = 0,
                 validated_persons: int = 0,
                 validated_places: int = 0,
                 validated_tasks: int = 0,
                 validated_form_def: int = 0,
                 start_seq: str = None,
                 end_seq: str = None,
                 instance: str = 'mali-prod'
                 ):
        self.batch_id = batch_id
        self.start_at = start_at
        self.pending = pending
        self.end_at = end_at
        self.received = received
        self.received_forms = received_forms
        self.validated_forms = validated_forms
        self.malformed_forms = malformed_forms
        self.flatten_forms = flatten_forms
        self.validated_persons = validated_persons
        self.validated_places = validated_places
        self.validated_tasks = validated_tasks
        self.validated_form_def = validated_form_def
        self.start_seq = start_seq
        self.end_seq = end_seq
        self.instance = instance

