# Your Week in One Line

[![make.fun](https://make.fun/badge/u-boge-your-week-in-one-line-d1c14ced.svg)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-week-in-one-line-d1c14ced)
[![rank](https://make.fun/badge/u-boge-your-week-in-one-line-d1c14ced/ZQ051031/your-week-in-one-line-20261125/rank.svg)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-week-in-one-line-d1c14ced)
[![reward](https://make.fun/badge/u-boge-your-week-in-one-line-d1c14ced/ZQ051031/your-week-in-one-line-20261125/reward.svg)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-week-in-one-line-d1c14ced)

Entry for the [Your Week in One Line](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced) bounty on make.fun. The task: one line, at most 100 characters, that sums up the week — the win, the fail, the chaos, all of it.

## The line

> Won a chess crown, shipped five bounties, and still lost the week to one misplaced comma.

89 characters. The win is concrete (a chess crown, five bounties shipped); the fail is concrete too (one misplaced comma); the turn — winning everything except the week itself — is the joke. Nothing in it is filler, and it could only be this week.

## How it works

`main.py` (Python 3 standard library only, no network, no dependencies) writes the line to `/output/entry.txt` with no trailing newline. Before writing, it checks the line is a single non-blank line of at most 100 characters and refuses to write anything that would fail the gate. The output is deterministic: the same fixed string every run.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
