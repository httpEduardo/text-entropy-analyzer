# Entropy Scout

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

**Explore how varied or repetitive your text data is.**

Entropy Scout measures Shannon entropy across text and ranks lines by entropy. It can help you inspect vocabulary variety, find unusual lines, or compare text datasets before deeper analysis.

## Quick start

```bash
python entropy_scout.py --input sample.txt --mode word --top-lines 3
```

Use `--mode char` to measure character patterns, or add `--strip-whitespace` to ignore spaces in that mode.

## Options

| Option | Purpose |
| --- | --- |
| `--mode word\|char` | Analyze words or characters; defaults to `word`. |
| `--min-length N` | Skip lines with fewer tokens; defaults to `5`. |
| `--top-lines N` | Show the highest-entropy lines; defaults to `5`. |
| `--strip-whitespace` | Ignore whitespace when using character mode. |

The report includes overall entropy, token counts, and the lines with the highest entropy. These statistics describe text patterns; they do not determine whether content is meaningful or anomalous.

## License

[MIT](LICENSE)
