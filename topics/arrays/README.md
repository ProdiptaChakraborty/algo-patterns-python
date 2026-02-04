# Arrays

This section focuses on array-centric patterns that show up frequently in production code:
hash-based lookup, prefix sums for range-style reasoning, and linear scans with careful invariants.

## Patterns covered
- Hash map lookup (value → index / count)
- Prefix sums + frequency maps
- Two pointers and partitioning scans

## Implementations
- `lc_0001_two_sum.py` — Hash map complement lookup in a single pass (O(n) average).
- `lc_1752_check_if_array_is_sorted_and_rotated.py` — Count circular “drops”; valid rotation has at most one decrease (O(n) time, O(1) space).
- `lc_0026_remove_duplicates_from_sorted_array.py` — Two pointers (write index) to compact unique values in-place (O(n) time, O(1) space).
