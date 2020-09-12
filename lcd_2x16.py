import time
from typing import Final, Optional

import adafruit_character_lcd.character_lcd as character_lcd
import board
from digitalio import DigitalInOut

from module import *

# LCD CONFIG (4-bit mode) - You can use any GPIO data pins you want
RS: Final[DigitalInOut] = DigitalInOut(board.D26)
EN: Final[DigitalInOut] = DigitalInOut(board.D16)
D4: Final[DigitalInOut] = DigitalInOut(board.D17)
D5: Final[DigitalInOut] = DigitalInOut(board.D0)
D6: Final[DigitalInOut] = DigitalInOut(board.D6)
D7: Final[DigitalInOut] = DigitalInOut(board.D5)
COLUMNS: Final[int] = 16
ROWS: Final[int] = 2

LCD: Final[character_lcd.Character_LCD_Mono] = character_lcd.Character_LCD_Mono(
    RS, EN, D4, D5, D6, D7, COLUMNS, ROWS
)

INTERVAL: Final[float] = 10.0


def main() -> None:
    LCD.clear()

    stats_twitter: Optional[Stats] = None
    stats_gov: Optional[Stats] = None
    cpu_temperature: int
    gpu_temperature: int
    infected: int
    deaths: int

    while True:
        try:
            stats_twitter, stats_gov = ProcessExecutor.execute_pool([
                TwitterStatsGetter.get_stats,
                GovStatsGetter.get_stats
            ])
        except Exception:
            pass

        cpu_temperature = round(HardwareTempGetter.get_cpu_temp())
        gpu_temperature = round(HardwareTempGetter.get_gpu_temp())

        LCD.clear()

        if stats_twitter and stats_gov:
            infected = stats_twitter.infected if stats_twitter.infected > stats_gov.infected else stats_gov.infected
            deaths = stats_twitter.deaths if stats_twitter.deaths > stats_gov.deaths else stats_gov.deaths
            LCD.message = f"I:{infected} D:{deaths}\nCPU:{cpu_temperature} GPU:{gpu_temperature}"
        else:
            LCD.message = "Something went\nwrong"

        time.sleep(INTERVAL)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        LCD.clear()
