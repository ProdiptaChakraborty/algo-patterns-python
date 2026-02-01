# Arrays

This section focuses on array-centric patterns that show up frequently in production code:
hash-based lookup, prefix sums for range-style reasoning, and linear scans with careful invariants.

## Patterns covered
- Hash map lookup (value → index / count)
- Prefix sums + frequency maps
- Two pointers and partitioning scans

## Implementations
- `lc_0001_two_sum.py` — Hash map complement lookup in a single pass (O(n) average).
