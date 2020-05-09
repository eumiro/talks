import datetime as dt
from pathlib import Path

import matplotlib.pyplot as plt
import pytz


def plot_tz_offset_history(tz_filter=None, since_year=1890, until_year=2040):
    for tz_name in set(pytz.common_timezones) - {"GMT", "UTC"}:
        if tz_filter is not None and not tz_filter(tz_name):
            continue
        tz = pytz.timezone(tz_name)
        points = []
        for ts, (offset, _, _) in zip(tz._utc_transition_times, tz._transition_info):
            if points:
                points.append((ts, points[-1][1]))
            points.append((ts, offset.total_seconds() / 3600.0))
        points.append((dt.datetime.max, points[-1][1]))
        plt.plot(*zip(*points))

    plt.xlim(dt.datetime(since_year, 1, 1), dt.datetime(until_year, 12, 31))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_tz_offset_history()
    # plot_tz_offset_history(
    #     tz_filter=lambda x: x.startswith("Europe/"), since_year=1970, until_year=1985
    # )
