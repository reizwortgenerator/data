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
            ("SPIEGEL_PANORAMA", "https://www.spiegel.de/panorama/index.rss"),
            (
                "BILD_LIFESTYLE",
                "https://www.bild.de/rssfeeds/vw-lifestyle/vw-lifestyle-16728898,dzbildplus=true,short=1,sort=1,teaserbildmobil=false,view=rss2.bild.xml",
            ),
            ("FAZ_POLITIK", "https://www.faz.net/rss/aktuell/politik/"),
            ("SUEDDEUTSCHE_POLITIK", "https://rss.sueddeutsche.de/rss/Politik"),
        ]:
            yield scrapy.http.Request(url, cb_kwargs={"key": key})

    def parse(self, response, key):
        yield {
            "_key": key,
            "_fetched_at": datetime.now(timezone.utc).isoformat(),
            "data": response.body.decode("utf-8"),
        }
