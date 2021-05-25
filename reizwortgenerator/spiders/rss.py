from datetime import datetime, timezone
import scrapy


class RssSpider(scrapy.Spider):
    name = "rss"

    def start_requests(self):
        for (key, url) in [
            ("CSU", "https://www.csu.de/rss/"),
            ("SPD", "https://www.spd.de/aktuelles/feed.rss"),
            ("AFD", "https://afdkompakt.de/feed/"),
            ("LINKE", "https://www.die-linke.de/start/presse/feed.rss"),
            ("GRUENE", "https://www.gruene.de/feeds/neues.html"),
        ]:
            yield scrapy.http.Request(url, cb_kwargs={"key": key})

    def parse(self, response, key):
        yield {
            "_key": key,
            "_fetched_at": datetime.now(timezone.utc).isoformat(),
            "data": response.body.decode("utf-8"),
        }
