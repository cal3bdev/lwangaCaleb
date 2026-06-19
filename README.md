# Recess Python — lwangaCaleb

Python practice assignments for the recess term. Each program is a
self-contained, menu- or input-driven console application.

## Requirements

- Python 3.10+ (assignment 2 uses `match`/`case`)

Run any program from this directory:

```bash
python3 assignment2.py
```

## Assignments

| # | File | Topic | What it does |
|---|------|-------|--------------|
| 1 | `bill split calculator.py` | Input, validation, f-strings | Splits a bill across people with a tip, prints a receipt, and can rerun. |
| 2 | `assignment2.py` | Control structures (`match`/`case`), login loop | E-commerce checkout: authenticates a user, then applies a coupon discount and location-based tax to a subtotal. |
| 3 | `assignment3.py` | Functions, loops, `random` | 2026 FIFA World Cup team manager simulation across prep, group, and knockout stages; tactical choices affect morale, injuries, and strength. |
| 4 | `assignment4.py` | Functions, menu loop, error handling | Menu-driven calculator (add, subtract, multiply, divide) with input validation and divide-by-zero handling. |
| 5 | `assignment5.py` | Lists, tuples, CRUD | Contact manager: add, view, update, delete, search, and list contacts, with phone and email validation. |

## Reference data

**Assignment 2 — login:** username `Cashier`, password `password` (3 attempts).

| Coupon | Discount | | Country | Tax |
|--------|----------|---|---------|-----|
| `CU435x` | 10% | | Uganda / Tanzania / Rwanda | 18% |
| `Yu234C` | 40% | | Kenya | 16% |
| `TY3345x` | 70% | | | |
