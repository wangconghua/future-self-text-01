#!/usr/bin/env python3
"""Texts From Your Future Self: one funny text from your future self.

Writes a single original text message (1-200 characters, one line) to
/output/entry.txt. The joke: the future self reports that you finally
become a morning person -- at 4am, because your back wakes you up before
your alarm does. The punchline lands on the last clause, the voice is a
specific future self texting back, and the angle is fresh (ageing, not
the obvious "still broke / still tired" joke).

Craft notes (from the kit's judge brief, most important first):
1. On subject: a funny text message from the writer's future self,
   written as if sent back to the present self, no setup outside it.
2. Lands a real joke with a twist that pays off by the last line.
3. Sounds like a specific future self: a concrete detail (the back,
   the alarm, 4am) that could only come from that person's life.
4. Uses the characters well: no wasted words, punchline arrives fast.
5. Fresh angle: becoming a morning person via a bad back, not the
   obvious broke/tired joke.
"""

import os

# The entry text. Filled in by a second, separate edit so the program
# (checks first) and the joke (second) each get their own revision.
ENTRY_TEXT = (
    "Future you here: you do become a morning person. At 4am. "
    "Because your back wakes you up before your alarm does."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def check_is_text(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")


def check_not_blank(text):
    if not text.strip():
        raise ValueError("entry must not be only white space")


def check_length(text):
    n = len(text)
    if n < MIN_CHARS or n > MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, n)
        )


def check_single_line(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_text_voice(text):
    """Reads like a text message from the future self: it names itself
    as the future self and addresses the present self directly."""
    lowered = text.lower()
    future_markers = ("future you", "future me", "from 20", "it's me", "its me")
    if not any(m in lowered for m in future_markers):
        raise ValueError("entry must identify itself as the future self")
    if "you" not in lowered:
        raise ValueError("entry must address the present self ('you')")


def check_ends_with_punctuation(text):
    if text[-1] not in ".!?":
        raise ValueError("entry must end with sentence punctuation")


def check_no_excess_whitespace(text):
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")
    if "  " in text or "\t" in text:
        raise ValueError("entry must not contain double spaces or tabs")


def check_utf8(text):
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable


CHECKS = (
    check_is_text,
    check_not_blank,
    check_length,
    check_single_line,
    check_text_voice,
    check_ends_with_punctuation,
    check_no_excess_whitespace,
    check_utf8,
)


def validate(text):
    for check in CHECKS:
        check(text)
    return text


def main():
    text = validate(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))


if __name__ == "__main__":
    main()
