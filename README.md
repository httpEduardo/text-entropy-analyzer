# Entropy Scout

Entropy Scout measures Shannon entropy and perplexity to spot noisy or repetitive lines in datasets.

## Quick start

```bash
python entropy_scout.py --input sample.txt --mode word --top-lines 3
```

## Options

- `--mode`: `char` or `word` (default: word).
- `--min-length`: Minimum token count per line (default: 5).
- `--top-lines`: Number of high-entropy lines to display.
- `--strip-whitespace`: Ignore whitespace tokens in char mode.

## Output

The report includes global entropy, top tokens, and outlier lines.
