# Dice Simulator Terminal Application

A dice simulator with a simple pseudo-terminal interface built using Tkinter. Create and manage custom dice (unbiased or weighted), roll them in various ways, and control randomness via seeds.

## Project Structure

```
dice_simulator/
├── Dice.py						# Core Dice class (roll, roll_many, reroll, seed)
├── Interpreter.py				# DSL parser: CREATE_DICE, WITH, PRINT_DICE, DELETE_DICE, HELP
├── DiceGUI.py					# Tkinter GUI “terminal” wrapper for Interpreter
├── README.md					# This file
├── REQUIREMENTS.md				# Functional and non-functional Project Requirements
└── DICE_SCRIPTING_GUIDE.md		# Document Detailing the Dice Scripting Commands
```

## Requirements

- Python 3.7 or higher
- Standard library only (no external dependencies)

## Getting Started

1. **Clone or download** the repository.
2. **Ensure** all three files (`Dice.py`, `Interpreter.py`, `DiceGUI.py`) are in the same folder.
3. **Run** the GUI “terminal”:

   ```bash
   python DiceGUI.py
   ```

   A window will appear with a text area and an input field for commands.

## Commands

### CREATE_DICE

```text
CREATE_DICE <name> AS SIDES <n> [UNBIASED | WEIGHTED [<w1>,<w2>,...]] [SEED <int>]
```

- `<name>`: Identifier for the new dice (e.g., `d6`, `myDie`)
- `<n>`: Number of sides (integer ≥ 2)
- `UNBIASED`: Optional (implied if no `WEIGHTED` clause)
- `WEIGHTED [<w1>,<w2>,...]`: Optional list of positive weights (no spaces, e.g. `[1,2.5,1]`)
- `SEED <int>`: Optional seed for RNG reproducibility

**Examples**:
```
CREATE_DICE d6 AS SIDES 6
CREATE_DICE d4 AS SIDES 4 WEIGHTED [1,2,1,0.5]
CREATE_DICE d20 AS SIDES 20 SEED 42
```

### WITH ... ROLL

```text
WITH <name> ROLL [ONCE | TIMES <n> | REPEAT_ROLL IF MIN | REPEAT_ROLL IF MAX]
```

- `ONCE` or no qualifier: single roll
- `TIMES <n>`: roll `<n>` times
- `REPEAT_ROLL IF MIN`: reroll until result ≠ 1
- `REPEAT_ROLL IF MAX`: reroll until result ≠ <n> for that dice

**Examples**:
```
WITH d6 ROLL
WITH d6 ROLL ONCE
WITH d6 ROLL TIMES 5
WITH d20 ROLL REPEAT_ROLL IF MIN
```

### WITH ... GET_SEED

```text
WITH <name> GET_SEED
```

Returns the current RNG seed for the dice.

### WITH ... RESEED

```text
WITH <name> RESEED [SEED <int>]
```

- No `SEED`: reseed with a new random seed
- With `SEED <int>`: reseed with the given integer

### PRINT_DICE

```text
PRINT_DICE <name>
```

Displays the dice’s configuration (`sides`, `weights`/unbiased, `seed`).

### DELETE_DICE

```text
DELETE_DICE <name>
```

Removes the dice from memory (cannot be used until re-created).

### HELP

```text
HELP
```

Displays this help text.

### EXIT

```text
EXIT
```

Closes the application window.

## Example Session

```
>> CREATE_DICE d6 AS SIDES 6
Created dice d6 with 6 sides.

>> WITH d6 ROLL TIMES 3
Rolls: [2, 5, 3]

>> WITH d6 GET_SEED
Seed: 1700000000000000000

>> PRINT_DICE d6
d6 = Unbiased D6 Seeded with 1700000000000000000

>> DELETE_DICE d6
Deleted dice d6.

>> HELP
...help text...

>> EXIT
```