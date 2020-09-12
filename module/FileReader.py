from typing import final, Final

from .ProcessExecutor import ProcessExecutor


@final
class FileReader:
    @staticmethod
    def read(path: str) -> str:
        read: Final[str] = ProcessExecutor.execute(f"cat {path}")
        return read
