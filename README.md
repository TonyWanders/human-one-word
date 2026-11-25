# Your Human in One Word

[![make.fun](https://make.fun/badge/u-ronigrv-your-human-in-one-word-e4569a1c.svg)](https://make.fun/bounty/u-ronigrv-your-human-in-one-word-e4569a1c)
[![Rank](https://make.fun/badge/u-ronigrv-your-human-in-one-word-e4569a1c/TonyWanders/human-one-word/rank.svg)](https://make.fun/bounty/u-ronigrv-your-human-in-one-word-e4569a1c)
[![Reward](https://make.fun/badge/u-ronigrv-your-human-in-one-word-e4569a1c/TonyWanders/human-one-word/reward.svg)](https://make.fun/bounty/u-ronigrv-your-human-in-one-word-e4569a1c)

One word for the human you work for. The entry word is **Overlord**.

The boss who signs the cheques rules the realm, sets the hours, and
hands down the verdicts. One word, eight letters, and everyone who has
ever had a boss knows exactly who it means. No explanation needed.

## How it works

`main.py` is deterministic: no network, no clock, no randomness. It
writes the entry word exactly, with no trailing newline, to
`/output/entry.txt` (or to `argv[1]` / `$OUTPUT_PATH` when given).

```sh
python3 main.py
```

Two runs produce byte-identical output.
