
# CFG String Generator

This Python project implements a simple **Context-Free Grammar (CFG)** string generator, derivation tracker, and membership tester for the grammar:

    S → aSb | ε

The grammar generates strings where the number of `a`s is equal to the number of `b`s and follows a balanced nesting (e.g. `ab`, `aabb`, `aaabbb`, etc.).

## Features

- ✅ Random generation of strings from the CFG
- ✅ Generates up to 10 strings of length ≤ specified maximum
- ✅ Computes a derivation sequence for any given valid string
- ✅ Tests if a given string belongs to the language defined by the CFG

## Example Usage

```python
cfg = CFG()

# Generate up to 10 random strings with maximum length 10
print(cfg.get_random_strings(10))

# Print a derivation sequence for a given string
print(cfg.get_derivation("aaaabbbb"))

# Test if a given string is in the language
print(cfg.membership_test("ab"))
