from typing import final, Final


@final
class Stats:
    @property
    def infected(self) -> int:
        return self.__infected

    @property
    def deaths(self) -> int:
        return self.__deaths

    def __init__(self, infected: int, deaths: int) -> None:
        self.__infected: Final[int] = infected
        self.__deaths: Final[int] = deaths

    @staticmethod
    def parse_record(record: str) -> int:
        parsed_record = int(''.join(record.split()))
        return parsed_record
