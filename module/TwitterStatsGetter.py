import re
from typing import final, Final, Optional, Pattern, AnyStr

import requests
from bs4 import BeautifulSoup

from .Stats import Stats
from .StatsGetter import StatsGetter


@final
class TwitterStatsGetter(StatsGetter):
    URL: Final[str] = 'https://mobile.twitter.com/MZ_GOV_PL'
    PHRASE: Final[Pattern[AnyStr]] = re.compile('koronawirusem:')
    STATS_PATTERN: Final[str] = r'(\d+\s\d+)/(\d+\s\d+)'

    @classmethod
    def get_stats(cls) -> Optional[Stats]:
        req: Final[requests.Response] = requests.get(cls.URL)
        if req.status_code == 200:
            soup: Final[BeautifulSoup] = BeautifulSoup(req.text, 'html.parser')
            found: Final[re.Match] = re.search(cls.STATS_PATTERN, soup.find(string=cls.PHRASE))
            infected: int = Stats.parse_record(found.group(1))
            deaths: int = Stats.parse_record(found.group(2))

            return Stats(infected, deaths)

        return None
