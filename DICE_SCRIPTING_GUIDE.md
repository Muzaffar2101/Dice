
# Dice Scripting Language Guide

This scripting language is designed to interact with a customizable Dice Simulator. It supports creating, rolling, reseeding, inspecting, and deleting virtual dice.

---

## 🎲 Dice Creation

### Syntax
```
CREATE_DICE <name> AS SIDES <n> [UNBIASED | WEIGHTED [<w1>,<w2>,...]] [SEED <int>]
```

### Examples
```
CREATE_DICE d6 AS SIDES 6
CREATE_DICE lucky AS SIDES 6 WEIGHTED [1,1,1,1,1,10] SEED 1234
```

### Notes
- `<name>` is the unique identifier for the dice.
- `<n>` must be an integer ≥ 2.
- If `WEIGHTED` is omitted, the dice is considered UNBIASED.
- `WEIGHTED` takes a comma-separated list of numbers inside brackets `[ ]` with **no spaces**.
- `SEED` allows reproducible randomness.

---

## 🎯 Rolling Dice

### Syntax
```
WITH <name> ROLL [ONCE | TIMES <n> | REPEAT_ROLL IF MIN | REPEAT_ROLL IF MAX]
```

### Examples
```
WITH d6 ROLL ONCE
WITH d6 ROLL TIMES 5
WITH lucky ROLL REPEAT_ROLL IF MIN
```

### Notes
- `REPEAT_ROLL IF MIN` rolls until a non-minimum value occurs.
- `REPEAT_ROLL IF MAX` rolls until a non-maximum value occurs.

---

## 🔁 Reseeding Dice

### Syntax
```
WITH <name> RESEED [<new_seed>]
```

### Examples
```
WITH d6 RESEED
WITH lucky RESEED 999
```

### Notes
- Without a seed, a new random one is used.
- Seed allows reproducible behavior.

---

## 🧪 Inspecting Dice

### Get Current Seed
```
WITH <name> GET_SEED
```

### Print Internal State
```
PRINT_DICE <name>
```

### Examples
```
WITH lucky GET_SEED
PRINT_DICE d6
```

---

## ❌ Deleting Dice

### Syntax
```
DELETE_DICE <name>
```

### Example
```
DELETE_DICE d6
```

### Notes
- Removes the dice from memory.

---

## 🆘 Help and Exit

### Show Help
```
HELP
```

### Exit Program
```
EXIT
```

---

## 🚫 Error Handling

- Invalid commands return `"Invalid command!"`
- Improper syntax or nonexistent dice return `"Error: <message>"`

---

## 🔧 Implementation Notes

- All commands are **case-sensitive**.
- Inputs are parsed by splitting on spaces; avoid extra whitespace.
