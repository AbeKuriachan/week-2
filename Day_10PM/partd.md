# AI Code Review Assignment — `analyze_text` Module

---

## Step 1 — Exact Prompt Sent to Claude

> "Write a Python module with a function called `analyze_text(text: str, **options)` that accepts any text
> and keyword arguments for options (`count_words=True`, `count_sentences=True`,
> `find_longest_word=True`, `sentiment_simple=True`). Each option enables a different analysis.
> Use `*args` and `**kwargs`, add type hints and Google-style docstrings. Return a dict with all
> requested analyses."

**Model used:** Claude (claude-sonnet-4-6)  
**Date:** 2025

---

## Step 2 — AI's Raw Output Code

```python
"""
Text Analysis Module

This module provides functions for analyzing text, including word counting,
sentence counting, finding the longest word, and simple sentiment analysis.
"""

from typing import Any


def analyze_text(text: str, **options: Any) -> dict[str, Any]:
    """Analyzes text based on specified options.

    This function performs various text analyses based on the provided options.
    By default, all analyses are performed if no options are specified.

    Args:
        text: The input text to analyze.
        **options: Keyword arguments for analysis options:
            count_words (bool): Count the number of words. Defaults to True.
            count_sentences (bool): Count the number of sentences. Defaults to True.
            find_longest_word (bool): Find the longest word. Defaults to True.
            sentiment_simple (bool): Perform simple sentiment analysis. Defaults to True.

    Returns:
        A dictionary containing the results of requested analyses.
        Possible keys include:
            - 'word_count' (int): Number of words in the text.
            - 'sentence_count' (int): Number of sentences in the text.
            - 'longest_word' (str): The longest word found in the text.
            - 'sentiment' (str): Simple sentiment ('positive', 'negative', or 'neutral').

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> result = analyze_text("Hello world! This is great.", count_words=True)
        >>> print(result['word_count'])
        5
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    # Default all options to True if not specified
    count_words = options.get('count_words', True)
    count_sentences = options.get('count_sentences', True)
    find_longest_word = options.get('find_longest_word', True)
    sentiment_simple = options.get('sentiment_simple', True)

    results: dict[str, Any] = {}

    if count_words:
        words = text.split()
        results['word_count'] = len(words)

    if count_sentences:
        import re
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        results['sentence_count'] = len(sentences)

    if find_longest_word:
        import re
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        if words:
            results['longest_word'] = max(words, key=len)
        else:
            results['longest_word'] = ''

    if sentiment_simple:
        positive_words = {'good', 'great', 'excellent', 'happy', 'wonderful',
                         'amazing', 'fantastic', 'love', 'best', 'awesome'}
        negative_words = {'bad', 'terrible', 'awful', 'hate', 'worst',
                         'horrible', 'disgusting', 'poor', 'sad', 'disappointing'}

        words = set(text.lower().split())
        positive_count = len(words & positive_words)
        negative_count = len(words & negative_words)

        if positive_count > negative_count:
            results['sentiment'] = 'positive'
        elif negative_count > positive_count:
            results['sentiment'] = 'negative'
        else:
            results['sentiment'] = 'neutral'

    return results


def process_multiple_texts(*args: str, **options: Any) -> list[dict[str, Any]]:
    """Process multiple texts with the same analysis options.

    Args:
        *args: Variable number of text strings to analyze.
        **options: Analysis options passed to analyze_text().

    Returns:
        A list of dictionaries, each containing analysis results for
        the corresponding input text.

    Raises:
        TypeError: If any argument is not a string.

    Example:
        >>> results = process_multiple_texts("Hello world!", "Goodbye!", count_words=True)
        >>> print(len(results))
        2
    """
    return [analyze_text(text, **options) for text in args]
```

---

## Step 3 — Critical Evaluation

### ✅ Does it properly use `**kwargs`?

**Partially — with a design flaw.**

The function signature correctly uses `**options` to capture keyword arguments, and
`options.get('key', True)` is used to read them. However, there is a subtle but
important issue: **all options default to `True`**. This means calling
`analyze_text("hello", count_words=False)` still runs the other three analyses the
caller never asked for. A cleaner contract would be: *"if you pass no options, run
everything; if you pass any options, run only what's explicitly requested."*

There is also no guard against **unknown kwargs** — passing
`analyze_text("hi", typo_option=True)` silently does nothing instead of warning the caller.

```python
# AI's approach — all four analyses run unless each is individually disabled
count_words = options.get('count_words', True)   # default True
```

---

### ✅ Are type hints correct?

Mostly yes. `text: str`, `**options: Any`, and `-> dict[str, Any]` are all valid.
Minor nits:

- `**options: Any` types *each value* as `Any`; the more precise annotation would be
  `**options: bool` since every expected value is a boolean flag.
- The return dict has mixed value types (`int`, `str`). Using `dict[str, Any]` is
  pragmatic here, though a `TypedDict` would be ideal for a production module.

---

### ⚠️ Does it handle edge cases?

| Edge Case | Handled? | Notes |
|-----------|----------|-------|
| Non-string input | ✅ Yes | Raises `TypeError` |
| Empty string `""` | ⚠️ Partial | Returns `word_count=0`, `longest_word=''`, but `sentence_count=0` and `sentiment='neutral'` — all technically correct, but no explicit check or documentation |
| Whitespace-only `"   "` | ⚠️ Partial | `word_count=0`, `longest_word=''` — correct but untested/undocumented |
| No options passed | ⚠️ Ambiguous | Runs everything by default — undocumented behaviour |
| Unknown option key | ❌ No | Silently ignored; should warn |
| Punctuation-only text | ✅ Handled | `re.findall(r'\b[a-zA-Z]+\b', ...)` correctly returns `[]` |

---

### ⚠️ Is the docstring actually useful or just boilerplate?

The docstring is **above average for AI output** — it documents every option key and
every possible return key, includes a worked example, and lists the one exception
that can be raised. That said:

- The `Example` section only shows `count_words=True` — it should also show the
  selective-option pattern and what an empty-text call returns.
- The description "Analyzes text based on specified options" is tautological.
- There is no mention of the *default-all-True* behaviour, which is the most
  surprising aspect of the function.

---

### ❌ Does it follow the Single Responsibility Principle (SRP)?

**No.** `analyze_text` is a monolithic function with four distinct concerns bundled
inside one body behind `if` flags. Each analysis is a separate responsibility:

- Counting words
- Counting sentences
- Finding the longest word
- Scoring sentiment

This makes the function hard to test in isolation, hard to extend (adding a fifth
analysis grows the function further), and harder to reuse (you cannot import *just*
the sentiment scorer without pulling the whole function along).

The bonus `process_multiple_texts` is a nice addition that shows good use of `*args`,
but it cannot compensate for the monolith it wraps.

---

## Step 4 — Improved Version

### Design Decisions

1. **Split each analysis into its own function** — SRP, easy to unit-test.
2. **`analyze_text` becomes a clean orchestrator** — reads options, dispatches, returns.
3. **`sentiment_simple` uses a scored approach** — counts all matching words, not just
   the unique-word set intersection (fixes a subtle counting bug in the AI version).
4. **Edge cases are explicit** — empty/whitespace text handled at the top.
5. **Unknown kwargs raise `ValueError`** — fail loudly rather than silently.
6. **`count_words` uses a smarter split** — strips punctuation before counting.

---

```python
"""
text_analysis.py
================
A text analysis module demonstrating clean use of *args / **kwargs,
type hints, Google-style docstrings, and the Single Responsibility Principle.

Each analysis is implemented as a small, independently testable function.
``analyze_text`` acts purely as an orchestrator — it holds no analysis logic itself.
"""

import re
from typing import Any


# ──────────────────────────────────────────────────────────────────────────────
# Individual analysis functions (Single Responsibility)
# ──────────────────────────────────────────────────────────────────────────────

def count_words(text: str) -> int:
    """Count the number of words in *text*.

    A "word" is any non-whitespace token after stripping leading/trailing
    punctuation. An empty or whitespace-only string returns 0.

    Args:
        text: The input string to count words in.

    Returns:
        The number of words found (>= 0).

    Examples:
        >>> count_words("Hello, world!")
        2
        >>> count_words("   ")
        0
    """
    tokens = text.split()
    # Strip surrounding punctuation so "world!" and "world" both count as words
    words = [re.sub(r"^\W+|\W+$", "", t) for t in tokens]
    return len([w for w in words if w])


def count_sentences(text: str) -> int:
    """Count the number of sentences in *text*.

    Sentence boundaries are detected at `.`, `!`, and `?` characters.
    Consecutive terminators (e.g. `"Wait..."`) are treated as one boundary.

    Args:
        text: The input string to count sentences in.

    Returns:
        The number of sentences found (>= 0).

    Examples:
        >>> count_sentences("Hi there. How are you? Great!")
        3
        >>> count_sentences("")
        0
    """
    if not text.strip():
        return 0
    parts = re.split(r"[.!?]+", text)
    return len([p for p in parts if p.strip()])


def find_longest_word(text: str) -> str:
    """Return the longest alphabetic word in *text*.

    Only sequences of ASCII letters are considered. If multiple words share
    the maximum length, the first occurrence is returned.

    Args:
        text: The input string to search.

    Returns:
        The longest word found, or an empty string if no alphabetic words exist.

    Examples:
        >>> find_longest_word("The quick brown fox")
        'quick'
        >>> find_longest_word("123 !!!")
        ''
    """
    words = re.findall(r"[a-zA-Z]+", text)
    if not words:
        return ""
    return max(words, key=len)


# Sentiment word lists — defined at module level so they are created once,
# not on every function call (which was a hidden performance issue in the AI version).
_POSITIVE_WORDS: frozenset[str] = frozenset({
    "good", "great", "excellent", "happy", "wonderful", "amazing",
    "fantastic", "love", "best", "awesome", "joy", "superb", "brilliant",
})
_NEGATIVE_WORDS: frozenset[str] = frozenset({
    "bad", "terrible", "awful", "hate", "worst", "horrible",
    "disgusting", "poor", "sad", "disappointing", "dreadful", "miserable",
})


def sentiment_simple(text: str) -> str:
    """Classify *text* sentiment as ``'positive'``, ``'negative'``, or ``'neutral'``.

    Uses a keyword-matching approach: counts all occurrences of positive and
    negative words (not just unique ones), then compares the totals.

    Args:
        text: The input string to classify.

    Returns:
        ``'positive'`` if positive keywords outnumber negative ones,
        ``'negative'`` if negative keywords outnumber positive ones,
        ``'neutral'`` otherwise (including empty input).

    Examples:
        >>> sentiment_simple("This is great and amazing!")
        'positive'
        >>> sentiment_simple("Terrible and awful experience.")
        'negative'
        >>> sentiment_simple("")
        'neutral'
    """
    if not text.strip():
        return "neutral"

    # Count ALL occurrences (not just unique), fixing the AI version's subtle bug:
    # "great great great bad" should score positive, not neutral.
    tokens = re.findall(r"[a-zA-Z]+", text.lower())
    positive_score = sum(1 for t in tokens if t in _POSITIVE_WORDS)
    negative_score = sum(1 for t in tokens if t in _NEGATIVE_WORDS)

    if positive_score > negative_score:
        return "positive"
    if negative_score > positive_score:
        return "negative"
    return "neutral"


# ──────────────────────────────────────────────────────────────────────────────
# Orchestrator
# ──────────────────────────────────────────────────────────────────────────────

# Maps every recognised option key → the function that handles it
_ANALYSIS_REGISTRY: dict[str, Any] = {
    "count_words":      count_words,
    "count_sentences":  count_sentences,
    "find_longest_word": find_longest_word,
    "sentiment_simple": sentiment_simple,
}


def analyze_text(text: str, **options: bool) -> dict[str, Any]:
    """Run selected text analyses and return the combined results.

    Each keyword argument corresponds to one analysis. Pass the option as
    ``True`` to include it in the output. If **no** options are provided,
    **all** analyses are run by default.

    Args:
        text: The input string to analyse. Must be a ``str``; may be empty.
        **options: Boolean flags controlling which analyses to run:

            * ``count_words``      (bool): Number of words.
            * ``count_sentences``  (bool): Number of sentences.
            * ``find_longest_word`` (bool): Longest alphabetic word.
            * ``sentiment_simple`` (bool): Simple sentiment label.

    Returns:
        A ``dict`` whose keys are a subset of:

        .. code-block:: python

            {
                "word_count":     int,   # present if count_words=True
                "sentence_count": int,   # present if count_sentences=True
                "longest_word":   str,   # present if find_longest_word=True
                "sentiment":      str,   # present if sentiment_simple=True
            }

    Raises:
        TypeError:  If ``text`` is not a ``str``.
        ValueError: If an unrecognised option key is passed.

    Examples:
        >>> analyze_text("Hello world! This is great.")
        {'word_count': 5, 'sentence_count': 2, 'longest_word': 'Hello', 'sentiment': 'positive'}

        >>> analyze_text("Hello world!", count_words=True, sentiment_simple=True)
        {'word_count': 2, 'sentiment': 'neutral'}

        >>> analyze_text("")
        {'word_count': 0, 'sentence_count': 0, 'longest_word': '', 'sentiment': 'neutral'}
    """
    # ── Input validation ──────────────────────────────────────────────────────
    if not isinstance(text, str):
        raise TypeError(f"'text' must be a str, got {type(text).__name__!r}")

    unknown = set(options) - set(_ANALYSIS_REGISTRY)
    if unknown:
        raise ValueError(
            f"Unknown option(s): {sorted(unknown)}. "
            f"Valid options are: {sorted(_ANALYSIS_REGISTRY)}"
        )

    # ── Determine which analyses to run ───────────────────────────────────────
    # If no options are specified → run everything.
    # If any options are specified → run only the ones explicitly set to True.
    if not options:
        active = set(_ANALYSIS_REGISTRY)
    else:
        active = {key for key, enabled in options.items() if enabled}

    # ── Output key names (kept separate from function names for clean API) ────
    _output_keys: dict[str, str] = {
        "count_words":       "word_count",
        "count_sentences":   "sentence_count",
        "find_longest_word": "longest_word",
        "sentiment_simple":  "sentiment",
    }

    # ── Dispatch ──────────────────────────────────────────────────────────────
    results: dict[str, Any] = {}
    for option in active:
        analysis_fn = _ANALYSIS_REGISTRY[option]
        results[_output_keys[option]] = analysis_fn(text)

    return results


# ──────────────────────────────────────────────────────────────────────────────
# Batch helper (demonstrates *args)
# ──────────────────────────────────────────────────────────────────────────────

def analyze_multiple(*texts: str, **options: bool) -> list[dict[str, Any]]:
    """Analyse multiple texts with the same set of options.

    Args:
        *texts:   One or more strings to analyse.
        **options: Analysis flags forwarded unchanged to :func:`analyze_text`.

    Returns:
        A list of result dicts, one per input text, in the same order.

    Raises:
        TypeError:  If any element of ``texts`` is not a ``str``.
        ValueError: If an unrecognised option key is passed.

    Examples:
        >>> analyze_multiple("Great day!", "Awful day!", sentiment_simple=True)
        [{'sentiment': 'positive'}, {'sentiment': 'negative'}]
    """
    return [analyze_text(t, **options) for t in texts]


# ──────────────────────────────────────────────────────────────────────────────
# Quick demo
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sample = "Python is an amazing language. Writing clean code is great!"

    print("── All analyses (no options → default all) ──")
    print(analyze_text(sample))

    print("\n── Selective: words + sentiment only ──")
    print(analyze_text(sample, count_words=True, sentiment_simple=True))

    print("\n── Empty string ──")
    print(analyze_text(""))

    print("\n── Batch analysis ──")
    for result in analyze_multiple("Wonderful!", "Terrible.", count_words=True, sentiment_simple=True):
        print(result)
```

---

## Comparison Table

| Criterion | AI Version | Improved Version |
|-----------|-----------|------------------|
| `**kwargs` usage | ✅ Uses `options.get()` correctly | ✅ Same + validates unknown keys |
| Type hints | ✅ `dict[str, Any]` | ✅ `**options: bool`, `frozenset[str]` |
| Empty string | ⚠️ Works but untested/undocumented | ✅ Explicit check + documented |
| Unknown option | ❌ Silently ignored | ✅ Raises `ValueError` |
| Docstring quality | ⚠️ Good skeleton, missing edge cases | ✅ All edge cases + return shape documented |
| SRP | ❌ Monolithic — 4 concerns in 1 function | ✅ 4 small functions + 1 orchestrator |
| Testability | ⚠️ Must test via `analyze_text` | ✅ Each analyser testable independently |
| Sentiment scoring | ⚠️ Unique-word set intersection (loses duplicates) | ✅ Counts all occurrences |
| Sentiment words | ⚠️ Recreated on every call | ✅ Module-level `frozenset` — created once |
| Registry pattern | ❌ Hard-coded `if` blocks | ✅ `_ANALYSIS_REGISTRY` dict — easy to extend |
| `*args` usage | ✅ In `process_multiple_texts` | ✅ In `analyze_multiple` |

---

## Key Takeaways

1. **AI code is a strong first draft, not a finished product.** The structure was correct
   but the design was monolithic and had a silent-failure mode on unknown options.

2. **SRP matters more than line count.** The improved version is longer, but each function
   has one job, making it far easier to test, maintain, and extend.

3. **Defaults should be explicit and documented.** The AI's "all options default True"
   behaviour was surprising and undocumented — a common source of bugs.

4. **Small performance details add up.** Creating a `set` of 500 sentiment words inside
   a function that might be called thousands of times is wasteful; a module-level
   `frozenset` is the right tool.

5. **A registry pattern (`dict` of option → function) scales better than chained `if`
   blocks** — adding a sixth analysis option is a one-line change, not a surgery.