# Dice Simulator Terminal Application — Requirements Document

## 1. Introduction

### 1.1 Purpose  
This document describes the requirements for the **Dice Simulator**, a terminal-style application (with optional GUI wrapper) that allows users to create, configure, roll, and manage custom dice for tabletop games, simulations, or statistical experiments.

### 1.2 Scope  
The Dice Simulator provides:  
- Creation of unbiased or weighted N-sided dice  
- Controlled randomness via seeding and reseeding  
- Multiple roll operations (single, batch, conditional rerolls)  
- Interactive command interface (CLI/GUI “terminal”)  
- Management commands (print, delete, help, exit)

### 1.3 Definitions, Acronyms, Abbreviations  
- **Die / Dice**: An N-sided random number generator.  
- **CLI**: Command-Line Interface.  
- **GUI**: Graphical User Interface (here, a Tkinter “terminal”).  
- **RNG**: Random Number Generator.  
- **SRS**: Software Requirements Specification.

### 1.4 References  
- IEEE Std 830-1998, “Recommended Practice for Software Requirements Specifications”  
- Python 3.7+ documentation  
- Tkinter GUI library documentation

### 1.5 Overview  
Section 2 gives the overall product description; Section 3 enumerates detailed functional requirements; Section 4 covers interfaces; Section 5 covers non-functional requirements.

---

## 2. Overall Description

### 2.1 Product Perspective  
- A standalone Python application, no external dependencies beyond the standard library.  
- Consists of three modules:
  1. `Dice.py` (core class)  
  2. `Interpreter.py` (command parser)  
  3. `DiceGUI.py` (Tkinter wrapper)

### 2.2 Product Functions  
- Create, delete, and list (`PRINT_DICE`) dice objects  
- Roll dice (single, batch, conditional reroll)  
- Seed management (get, set, reseed)  
- Interactive help and exit

### 2.3 User Characteristics  
- Familiar with basic terminal commands  
- Some exposure to tabletop gaming concepts (e.g., “d6”)  
- No installation beyond Python interpreter required

### 2.4 Constraints  
- Python 3.7+ must be installed  
- Weights list must be formatted without spaces (e.g., `[1,2.5,1]`)  
- Seed values are 64-bit integers

### 2.5 Assumptions & Dependencies  
- User will enter syntactically correct commands or use `HELP` to learn them.  
- RNG provided by Python’s `random.Random` is sufficient for statistical fairness.

---

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 Create Dice  
- **ID**: FR-1  
- **Description**:  
  `CREATE_DICE <name> AS SIDES <n> [UNBIASED | WEIGHTED [<w1>,<w2>,...]] [SEED <int>]`  
- **Inputs**: Dice name (string), number of sides (integer ≥ 2), optional weights (list of ≥ 1 non-negative floats, sum > 0), optional seed (integer).  
- **Behavior**:  
  - Reject if `<n> < 2`  
  - If `WEIGHTED` present, validate list length == n and contents match regex `(0|[1-9]\d*)(\.\d+)?`  
  - If all weights equal, treat as unbiased (drop weights)  
  - Store in registry under `<name>`.  
- **Outputs**: Confirmation string or error.

#### 3.1.2 Delete Dice  
- **ID**: FR-2  
- **Description**:  
  `DELETE_DICE <name>`  
- **Behavior**: Remove named dice from registry or error if not found.  
- **Output**: Confirmation or error.

#### 3.1.3 Print Dice  
- **ID**: FR-3  
- **Description**:  
  `PRINT_DICE <name>`  
- **Behavior**: Display sides, weights (or “Unbiased”), and seed via `__repr__()`.  
- **Output**: Formatted string or error.

#### 3.1.4 Roll Dice  
- **ID**: FR-4  
- **Description**:  
  `WITH <name> ROLL [ONCE | TIMES <k> | REPEAT_ROLL IF MIN | REPEAT_ROLL IF MAX]`  
- **Behavior**:  
  - `ONCE` or no qualifier: single roll → `Dice.roll()`  
  - `TIMES k`: batch → `Dice.roll_many(k)` (k ≥ 1)  
  - `REPEAT_ROLL IF MIN`: reroll until result ≠ 1 → `Dice.reroll_on_min()`  
  - `REPEAT_ROLL IF MAX`: reroll until result ≠ sides → `Dice.reroll_on_max()`  
- **Output**: Single integer, list of integers, or list of reroll chain.

#### 3.1.5 Seed Management  
- **ID**: FR-5a `GET_SEED` → `WITH <name> GET_SEED` → return current seed.  
- **ID**: FR-5b `RESEED` → `WITH <name> RESEED [SEED <int>]` → set RNG to new or provided seed. Output confirmation.

#### 3.1.6 Help & Exit  
- **ID**: FR-6a `HELP` → display command summary.  
- **ID**: FR-6b `EXIT` → terminate application (CLI) or close window (GUI).

### 3.2 Error Handling  
- All parse errors or invalid operations return user-friendly error messages, never crash.

---

## 4. External Interface Requirements

### 4.1 User Interfaces  
- **CLI**: Terminal I/O for `Interpreter.py`.  
- **GUI**: Tkinter window (`DiceGUI.py`) with:
  - Scrollable text area (output)  
  - Single-line entry box (input)  
  - Submit button  
  - Non-resizable maximized window

### 4.2 Software Interfaces  
- **Dice.py**: class `Dice` with methods:
  - `roll()`, `roll_many(k)`, `reroll_on_min()`, `reroll_on_max()`  
  - `get_seed()`, `reseed()`, `__repr__()`  
- **Interpreter.py**: functions:
  - `parse_create_dice()`, `parse_delete_dice()`, `parse_print_dice()`  
  - `parse_with_command()`, `print_help()`  
- **DiceGUI.py**: imports above and binds GUI controls.

---

## 5. Non-Functional Requirements

### 5.1 Performance  
- Rolling is O(k); conditional rerolls may be longer (acceptable).

### 5.2 Reliability  
- No crashes on invalid input; helpful errors displayed.

### 5.3 Portability  
- Runs on Windows, macOS, Linux with Python 3.7+.

### 5.4 Maintainability  
- Modular code, clear separation for class, parser, GUI.

### 5.5 Usability  
- SQL-like syntax, in-app HELP, GUI “terminal” avoids host clutter.

---

*End of Requirements Document*