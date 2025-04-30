import Interpreter

print("Welcome to the Dice CLI! Type 'HELP' for instructions. Type 'EXIT' to quit.")
while True:
    command = input(">> ").strip()
    if command.upper() == "EXIT":
        print("Goodbye!")
        break
    try:
        if command.startswith("CREATE_DICE"):
            print(Interpreter.parse_create_dice(command))
        elif command.startswith("WITH"):
            print(Interpreter.parse_with_command(command))
        elif command.startswith("PRINT_DICE"):
            print(Interpreter.parse_print_dice(command))
        elif command.startswith("DELETE_DICE"):
            print(Interpreter.parse_delete_dice(command))
        elif command == "HELP":
            Interpreter.print_help()
        else:
            print("Invalid command!")
    except Exception as e:
        print(f"Error: {e}")
