from typing import Final, final

from .FileReader import FileReader
from .ProcessExecutor import ProcessExecutor


@final
class HardwareTempGetter:
    CPU_SENSOR_PATH: Final[str] = '/sys/class/thermal/thermal_zone0/temp'
    GPU_COMMAND: Final[str] = 'vcgencmd measure_temp'

    @classmethod
    def get_cpu_temp(cls) -> float:
        read: Final[str] = FileReader.read(cls.CPU_SENSOR_PATH)
        temp: Final[float] = round(float(read) / 1000, 2)
        return temp

    @classmethod
    def get_gpu_temp(cls) -> float:
        read: Final[str] = ProcessExecutor.execute(cls.GPU_COMMAND)
        temp: Final[float] = float(read[read.index('=') + 1:read.index("'")])
        return temp
