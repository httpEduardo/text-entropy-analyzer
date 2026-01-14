import argparse
import math
import re
import sys
from collections import Counter

WORD_RE = re.compile(r"[a-zA-Z0-9']+")


def tokenize_words(text: str) -> list[str]:
    return WORD_RE.findall(text.lower())


def tokenize_chars(text: str, strip_ws: bool) -> list[str]:
    if strip_ws:
        return [ch for ch in text if not ch.isspace()]
    return list(text)


def shannon_entropy(tokens: list[str]) -> float:
    if not tokens:
        return 0.0
    total = len(tokens)
    counts = Counter(tokens)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy


def main() -> int:
    parser = argparse.ArgumentParser(description="Measure entropy across dataset lines.")
    parser.add_argument("--input", required=True, help="Path to input text file")
    parser.add_argument("--mode", choices=["char", "word"], default="word")
    parser.add_argument("--min-length", type=int, default=5)
    parser.add_argument("--top-lines", type=int, default=5)
    parser.add_argument("--strip-whitespace", action="store_true")
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as handle:
            lines = [line.rstrip("\n") for line in handle]
    except OSError as exc:
        print(f"Failed to read {args.input}: {exc}", file=sys.stderr)
        return 1

    records = []
    all_tokens: list[str] = []
    for idx, line in enumerate(lines, start=1):
        if args.mode == "word":
            tokens = tokenize_words(line)
        else:
            tokens = tokenize_chars(line, args.strip_whitespace)
        if len(tokens) < args.min_length:
            continue
        entropy = shannon_entropy(tokens)
        records.append({
            "line": idx,
            "text": line,
            "entropy": entropy,
            "tokens": tokens,
        })
        all_tokens.extend(tokens)

    if not records:
        print("No lines met the minimum token threshold.")
        return 0

    global_entropy = shannon_entropy(all_tokens)
    perplexity = 2 ** global_entropy
    counts = Counter(all_tokens)
    top_tokens = counts.most_common(8)

    print(f"Lines analyzed: {len(records)}")
    print(f"Global entropy: {global_entropy:.3f} bits")
    print(f"Perplexity: {perplexity:.2f}")
    print("\nTop tokens:")
    for token, count in top_tokens:
        print(f"  {token:>10}  {count}")

    records.sort(key=lambda item: item["entropy"], reverse=True)
    limit = min(args.top_lines, len(records))
    if limit > 0:
        print("\nHighest-entropy lines:")
        for item in records[:limit]:
            preview = item["text"].strip()
            if len(preview) > 72:
                preview = preview[:69] + "..."
            print(f"  #{item['line']:>3} {item['entropy']:.3f}  {preview}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
