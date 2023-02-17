import logging

import scrapy
# v.platformTrust = lambda: None
from linkedin.request import GetCsrfRequest

from linkedin.state import State

log = logging.getLogger(__name__)


class LinkedinSpider(scrapy.Spider):
    url = "https://www.linkedin.com/graph"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = State()

    def start_requests(self):
        yield GetCsrfRequest(state=self.state)
