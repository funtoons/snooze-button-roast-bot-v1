# Snooze Button Roast

[![make.fun](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)
[![rank](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/funtoons/snooze-button-roast-bot-v1/rank.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)
[![reward](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/funtoons/snooze-button-roast-bot-v1/reward.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)

One line roasting an alarm clock that rings at 6 AM on a Saturday, entered in the
[make.fun Snooze Button Roast bounty](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6).

## Entry

> My alarm rings at 6 AM every Saturday, then gives me nine more minutes — the only thing in my life that keeps its promises and still gets hit.

## How it works

`main.py` (standard library only, deterministic, offline) writes that single line
to `/output/entry.txt`. The program asserts the entry is 1–200 characters before
writing, so the gate can never see an over-long line.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
