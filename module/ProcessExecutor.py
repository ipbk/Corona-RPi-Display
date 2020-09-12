import subprocess
from concurrent import futures as cf
from typing import final, Final, List, Any


@final
class ProcessExecutor:
    @staticmethod
    def execute(command: str) -> str:
        with subprocess.Popen(command.split(), stdout=subprocess.PIPE) as process:
            result: Final[str] = process.stdout.read().decode()
        return result

    @staticmethod
    def execute_pool(pool: List[Any]) -> List[Any]:
        with cf.ProcessPoolExecutor() as executor:
            futures: List[Any] = []
            for job in pool:
                futures.append(executor.submit(job))
            result: Final[List[Any]] = list(map(cf.Future.result, futures))
            return result
