


"""## 👤 Person 1 — Load & parse the CSV
**Requirement:** read the CSV into a list of dicts. No pandas.
*(This is the loader we built — Person 1 owns it and can tweak; everyone else builds on `users`.)*
"""

import csv
def load_users(path):
  users = []
  with open(path, newline='') as f:
    reader= csv.DictReader(f)
    for row in reader:
      users.append({
          "name": row["Name"],
          "email": row["Email"],
          "age": int(row["Age"]),                                "city": row["City"],
          "purchase_amount": float(row["Purchase_Amount"]),
      })
    return users
users = load_users("C:\\Users\\Sunshine\\Documents\\PythonProjects\\user_data.csv")


"""## 👤 Person 2 — `filter()` + `map()`
**Req 1 (Filter):** use `filter()` + a lambda → users **over 30** who spent **more than $100**.
**Req 2 (Map):** use `map()` → list of just the **emails** for those users.
"""

# filter() and map() both return iterators -> wrap each in list().

# TODO: lambda should be True when age > 30 AND purchase_amount > 100

# TODO: pull just the "email" field out of each big_spender
big_spenders = list(filter(lambda u: u["age"] > 30 and  u["purchase_amount"] > 100, users))
big_spender_emails = list(map(lambda u: u["email"], big_spenders))
print("big spenders:", len(big_spenders))
  
for email in big_spender_emails[5:10]:  
    print( email)  # spot-check a few
    
print("\n")


"""## 👤 Person 3 — list comprehension (New York)
**Req 3:** build a list of `"Name: Age"` strings for users whose city is **"New York"**.
Must be a **list comprehension** — not a loop, not map/filter.
"""

# Shape:  [ <expression>  for u in users  if <condition> ]
# expression -> an f-string like f"{name}: {age}"
# condition  -> city equals "New York"

New_York_Users = [f'{user["name"]}: {user["age"]}' for user in users if user["city"] == "New York"]
print("New York users:", len(New_York_Users))
print(New_York_Users[5:10])
print("\n")

"""## 👤 Person 4 — `reduce()` total + sorting
**Req 4 (Reduce):** total purchase amount across the **whole** dataset, using `functools.reduce`.
**Req 5 (Sorting):** the **5 oldest** users, then print their names. Use a `key=` lambda.
"""

from functools import reduce

# Reduce: accumulate purchase_amount. Start value is 0.0.
# reduce(lambda acc, u: acc + ... , users, 0.0)
def total_spent(users):
  return reduce (lambda acc, u: acc+ float (u["purchase_amount"]), users, 0)

# Sort by age descending, take first 5.
def top5_oldest(users):
  sorted_users = sorted(users, key = lambda u: int(u["age"]), reverse=True)[:5]
  return [u["name"] for u in sorted_users]

"""## 👤 Person 5 — Integrator (final report)
Pull every result into one clean printout. **Run this LAST**, after cells 1–4 have all run.
If a name below is undefined, that person's cell hasn't been run yet.
"""

line = "=" * 44
top5_names = top5_oldest(users)
total_spent_value = total_spent(users)
print(line)
print("  LIST-PROCESSOR  —  FINAL REPORT")
print(line)
print(f"Total users loaded:        {len(users)}")
print(f"Over-30 big spenders:      {len(big_spenders)}")
print(f"  emails captured:         {len(big_spender_emails)}")
print(f"New York users:            {len(New_York_Users)}")
print(f"Total purchases:           ${total_spent_value:,.2f}")
print(f"5 oldest users:            {', '.join(top5_names)}")
print(line)

"""## ✅ Self-check targets
If these match, you're done:

| Piece | Expected |
|---|---|
| Users loaded | **1000** |
| Over-30 & >$100 | **632** |
| New York users | **172** |
| Total purchases | **$251,931.72** |

Spot-check the 5 oldest names by eye — all should be age 75 (or close).
"""