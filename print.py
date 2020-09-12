from typing import Optional

from module import *


def main():
    stats_twitter: Optional[Stats] = None
    stats_gov: Optional[Stats] = None
    cpu_temperature: int
    gpu_temperature: int

    try:
        stats_twitter, stats_gov = ProcessExecutor.execute_pool([
            TwitterStatsGetter.get_stats,
            GovStatsGetter.get_stats
        ])
    except Exception:
        pass

    cpu_temperature = round(HardwareTempGetter.get_cpu_temp())
    gpu_temperature = round(HardwareTempGetter.get_gpu_temp())

    if stats_twitter and stats_gov:
        print(f"Twitter: Infected: {stats_twitter.infected}, Deaths: {stats_twitter.deaths}")
        print(f"Gov: Infected: {stats_gov.infected}, Deaths: {stats_gov.deaths}")
    else:
        print("Something went wrong")

    print(f"CPU temperature: {cpu_temperature}, GPU Temperature: {gpu_temperature}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
