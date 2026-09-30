#!/usr/bin/env python3
"""
Pitch Timer — Analyze your pitch script for timing, word count, and pacing.

Usage:
    python3 pitch-timer.py                        Interactive mode (paste text)
    python3 pitch-timer.py --file pitch.txt       Analyze from file
    echo "Your pitch text" | python3 pitch-timer.py   Analyze from stdin
    python3 pitch-timer.py --file pitch.txt --target-minutes 10
                                                  Check against a custom length

Targets:
    30-second pitch: 75-90 words
    60-second pitch: 150-180 words
    2-minute pitch: 300-360 words
    3-minute pitch: 450-540 words
    N-minute pitch (--target-minutes N): N*130 to N*160 words
"""

import sys
import re


def analyze_text(text, target_minutes=None):
    """Analyze pitch text for timing and pacing."""
    words = text.split()
    word_count = len(words)

    # Average speaking rate: 150 words per minute (conversational)
    # Fast pace: 170 wpm
    # Slow pace: 130 wpm
    wpm_conversational = 150
    wpm_fast = 170
    wpm_slow = 130

    time_conversational = word_count / wpm_conversational
    time_fast = word_count / wpm_fast
    time_slow = word_count / wpm_slow

    # Sentence analysis
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)
    avg_words_per_sentence = word_count / max(sentence_count, 1)

    # Paragraph analysis
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    paragraph_count = len(paragraphs)

    # Readability (simple approximation)
    long_words = sum(1 for w in words if len(w) > 6)
    long_word_pct = (long_words / max(word_count, 1)) * 100

    # Determine target
    if target_minutes:
        low, high = int(target_minutes * 130), int(target_minutes * 160)
        target = f"{target_minutes:g}-minute pitch"
        target_range = f"{low}-{high} words"
        in_range = low <= word_count <= high
    elif word_count <= 90:
        target = "30-second pitch"
        target_range = "75-90 words"
        in_range = 75 <= word_count <= 90
    elif word_count <= 180:
        target = "60-second pitch"
        target_range = "150-180 words"
        in_range = 150 <= word_count <= 180
    elif word_count <= 360:
        target = "2-minute pitch"
        target_range = "300-360 words"
        in_range = 300 <= word_count <= 360
    elif word_count <= 540:
        target = "3-minute pitch"
        target_range = "450-540 words"
        in_range = 450 <= word_count <= 540
    else:
        target = "5+ minute pitch"
        target_range = "750-900 words"
        in_range = word_count >= 750

    # Pacing score
    if avg_words_per_sentence <= 15:
        pacing = "✅ Good — sentences are punchy and clear"
    elif avg_words_per_sentence <= 20:
        pacing = "🟡 OK — some sentences could be shorter"
    else:
        pacing = "🔴 Too long — break up long sentences"

    # Print report
    print("\n" + "=" * 55)
    print("  🎤 PITCH ANALYSIS REPORT")
    print("=" * 55)

    print(f"\n  📝 Word Count:     {word_count}")
    print(f"  🎯 Target:         {target} ({target_range})")
    if in_range:
        print(f"  ✅ Status:         In range!")
    else:
        print(f"  ⚠️  Status:         Outside target range")

    print(f"\n  ⏱️  Estimated Time:")
    print(f"     Fast pace:      {time_fast:.1f} minutes ({time_fast*60:.0f}s)")
    print(f"     Conversational: {time_conversational:.1f} minutes ({time_conversational*60:.0f}s)")
    print(f"     Slow pace:      {time_slow:.1f} minutes ({time_slow*60:.0f}s)")

    print(f"\n  📊 Structure:")
    print(f"     Sentences:      {sentence_count}")
    print(f"     Avg per sent:   {avg_words_per_sentence:.1f} words")
    print(f"     Paragraphs:     {paragraph_count}")
    print(f"     Long words:     {long_word_pct:.0f}% ({long_words} words)")

    print(f"\n  🎵 Pacing:         {pacing}")

    # Tips
    print(f"\n  💡 Tips:")
    if not in_range and target_minutes:
        if word_count < int(target_minutes * 130):
            print(f"     - Too short for {target_minutes:g} min: add a user story or demo narration")
        else:
            print(f"     - Too long for {target_minutes:g} min: cut features, keep 1-2 core ones")
    elif not in_range:
        if word_count < 75:
            print(f"     - Add more detail to your problem statement")
            print(f"     - Include a specific example or story")
            print(f"     - Explain the impact more clearly")
        elif word_count > 540:
            print(f"     - Cut features — focus on 1-2 core ones")
            print(f"     - Remove technical details judges won't understand")
            print(f"     - Shorten your opening hook")
    if avg_words_per_sentence > 20:
        print(f"     - Break long sentences into 2-3 shorter ones")
    if long_word_pct > 30:
        print(f"     - Replace complex words with simpler ones")
    if sentence_count < 5:
        print(f"     - Add more sentences for better pacing")

    print("\n" + "=" * 55 + "\n")

    return {
        "word_count": word_count,
        "time_seconds": time_conversational * 60,
        "target": target,
        "in_range": in_range,
        "sentences": sentence_count,
        "avg_words_per_sentence": avg_words_per_sentence
    }


def main():
    text = None
    args = sys.argv[1:]

    if "-h" in args or "--help" in args:
        print(__doc__)
        return

    target_minutes = None
    if "--target-minutes" in args:
        i = args.index("--target-minutes")
        try:
            target_minutes = float(args[i + 1])
            if target_minutes <= 0:
                raise ValueError
        except (IndexError, ValueError):
            print("  --target-minutes needs a positive number, e.g. --target-minutes 10")
            sys.exit(2)
        del args[i:i + 2]

    if len(args) > 1 and args[0] == "--file":
        try:
            with open(args[1], "r") as f:
                text = f.read()
        except FileNotFoundError:
            print(f"  File not found: {args[1]}")
            return
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        print("\n  📋 Paste your pitch script (press Enter twice when done):\n")
        lines = []
        empty_count = 0
        while True:
            try:
                line = input()
                if line == "":
                    empty_count += 1
                    if empty_count >= 2:
                        break
                    lines.append(line)
                else:
                    empty_count = 0
                    lines.append(line)
            except EOFError:
                break
        text = "\n".join(lines)

    if not text or not text.strip():
        print("  No text provided.")
        return

    analyze_text(text.strip(), target_minutes)


if __name__ == "__main__":
    main()
