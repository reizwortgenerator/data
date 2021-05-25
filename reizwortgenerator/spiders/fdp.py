from datetime import datetime, timezone
import scrapy

class FdpSpider(scrapy.Spider):
    name = "fdp"

    def start_requests(self):
        yield scrapy.http.Request(
            "https://www.fdp.de/uebersicht/artikel"
        )

    def parse(self, response):
        yield {
            "_key": "FDP",
            "_fetched_at": datetime.now(timezone.utc).isoformat(),
            "data": response.body.decode("utf-8"),
        }
