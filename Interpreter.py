import Dice
import re

# Dice Registry
dice_registry = {}

# Parser function
def parse_create_dice(command: str):
	parts = command.split()
	if parts[0] != "CREATE_DICE":
		raise ValueError("Invalid command")
	
	dice_name = parts[1]
	sides = int(parts[4])

	weights = None
	seed = None

	# Find where the "WEIGHTED" part is and extract weights from the next part
	if "WEIGHTED" in parts:
		weighted_index = parts.index("WEIGHTED")
		weights_str = parts[weighted_index + 1]

		# Ensure brackets are present
		if not (weights_str.startswith('[') and weights_str.endswith(']')):
			raise ValueError("Weights must be enclosed in brackets like [1,2,3] with no spaces.")

		# Strip brackets and validate comma-separated integers
		content = weights_str[1:-1]
		weights_parts = content.split(',')

		# Inline regex validator
		is_valid = lambda s: bool(re.fullmatch(r'(0|[1-9]\d*)(\.\d+)?', s))

		if not all(is_valid(part) for part in weights_parts):
			raise ValueError("Weights must be positive numbers (int or float) with no spaces.")

		weights = [float(part) for part in weights_parts]


	if "SEED" in parts:
		seed_index = parts.index("SEED")
		seed = int(parts[seed_index + 1])

	dice_registry[dice_name] = Dice.Dice(sides, weights, seed)
	return (f"Created dice {dice_name} with {sides} sides.")

def parse_delete_dice(command: str):
	parts = command.split()
	dice_name = parts[1]
	if dice_name in dice_registry:
		del dice_registry[dice_name]
		return (f"Deleted dice {dice_name}.")
	else:
		return (f"No dice found with name {dice_name}.")

def parse_print_dice(command: str):
	parts = command.split()
	dice_name = parts[1]
	if dice_name in dice_registry:
		return (f"{dice_name} = {dice_registry[dice_name]}")
	else:
		return (f"No dice found with name {dice_name}.")

def parse_with_command(command: str):
	parts = command.split()
	if parts[0] != "WITH":
		raise ValueError("Invalid command")

	dice_name = parts[1]
	if dice_name not in dice_registry:
		raise ValueError(f"No dice found with name {dice_name}")

	dice = dice_registry[dice_name]
	
	if parts[2] == "ROLL":
		if len(parts) == 3 or parts[3] == "ONCE":
			return(f"Roll: {dice.roll()}")
		elif parts[3] == "TIMES":
			count = int(parts[4])
			return(f"Rolls: {dice.roll_many(count)}")
		elif parts[3] == "REPEAT_ROLL" and parts[4] == "IF" and parts[5] == "MIN":
			return(f"Reroll chain: {dice.reroll_on_min()}")
		elif parts[3] == "REPEAT_ROLL" and parts[4] == "IF" and parts[5] == "MAX":
			return(f"Reroll chain: {dice.reroll_on_max()}")
	
	elif parts[2] == "GET_SEED":
		return(f"Seed: {dice.get_seed()}")
	
	elif parts[2] == "RESEED":
		if len(parts) == 3:
			dice.reseed()
			return(f"Dice reseeded with new seed.")
		elif len(parts) == 4:
			dice.reseed(int(parts[3]))
			return(f"Dice reseeded with seed {parts[3]}.")

def print_help():
	return("""
Available Commands:
-------------------

CREATE_DICE <name> AS SIDES <n> [UNBIASED | WEIGHTED [<w1>,<w2>,...]] [SEED <int>]
    - Create a new dice with specified number of sides.
    - Use WEIGHTED to give custom weights (no spaces in list).
    - UNBIASED is implied if WEIGHTED not used.
    - SEED is optional for reproducibility.

WITH <name> ROLL [ONCE | TIMES <n> | REPEAT_ROLL IF MIN | REPEAT_ROLL IF MAX]
    - Roll the dice once, multiple times, or with repeat-on-min/max condition.

WITH <name> GET_SEED
    - Show the seed used by the dice.

WITH <name> RESEED [SEED <int>]
    - Reseed the dice with a new or specific seed.
	   
DELETE_DICE <name>
    - Deletes a dice with the given name from memory.

PRINT_DICE <name>
    - Shows the internal state of the dice (sides, weights, seed).

HELP
    - Show this help message.

EXIT
    - Exit the simulator.
""")
