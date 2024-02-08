from typing import Dict


class HttpRequest:  # Pascal case
    def __init__(  # método construtor
        self, header: Dict = None, body: Dict = None, query_params: Dict = None
    ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params
