from typing import List


class CouchdbResponse:
    last_sequence_number: str
    pending: int
    docs: List[dict]
