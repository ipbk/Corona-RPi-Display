import json
from typing import final, Optional, Final, List

import requests
from bs4 import BeautifulSoup

from .Stats import Stats
from .StatsGetter import StatsGetter


@final
class GovStatsGetter(StatsGetter):
    URL: Final[str] = 'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2'
    SELECTOR: Final[str] = 'pre#registerData'
    INDEX: Final[str] = 'data'

    @classmethod
    def get_stats(cls) -> Optional[Stats]:
        req: Final[requests.Response] = requests.get(cls.URL)
        if req.status_code == 200:
            soup: Final[BeautifulSoup] = BeautifulSoup(req.text, 'html.parser')
            data: Final[dict] = json.loads(soup.select_one(cls.SELECTOR).text)
            stats: List[str] = data[cls.INDEX].split(';')[4:6]
            infected: int = Stats.parse_record(stats[0])
            deaths: int = Stats.parse_record(stats[1])

            return Stats(infected, deaths)

        return None
