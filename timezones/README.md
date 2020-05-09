# “A Day Has Only 24±1 Hours”

## `plot_tz_offset_history.py`

Plots a chart with all selected time zones offset over the years.

```python
plot_tz_offset_history(tz_filter, since_year, until_year)
```

- `tz_filter` (default `None` plots ALL time zones)
    - `lambda x: x == "Europe/Berlin"` plot only selected time zone
    - `lambda x: x.startswith("Europe/")` plot all European time zones
- `since_year` (default 1895)
- `until_year` (default 2040)


![`tz_offset_history.png`](tz_offset_history.png)

