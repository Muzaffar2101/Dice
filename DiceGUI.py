# DiceGUI.py
import tkinter as tk
import Interpreter

def handle_command():
    cmd = entry.get().strip()
    entry.delete(0, tk.END)
    if cmd.upper() == "EXIT":
        root.destroy()
        return
    try:
        if cmd.startswith("CREATE_DICE"):
            result = Interpreter.parse_create_dice(cmd)
        elif cmd.startswith("WITH"):
            result = Interpreter.parse_with_command(cmd)
        elif cmd.startswith("PRINT_DICE"):
            result = Interpreter.parse_print_dice(cmd)
        elif cmd.startswith("DELETE_DICE"):
            result = Interpreter.parse_delete_dice(cmd)
        elif cmd == "HELP":
            result = Interpreter.print_help()
        else:
            result = "Invalid command!"
    except Exception as e:
        result = f"Error: {e}"

    output(result)


def output(text):
    output_box.insert(tk.END, text + "\n")
    output_box.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("Dice Simulator")

# create a frame to hold the output
output_frame = tk.Frame(root)
# allow the frame to grow in both directions
output_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# create a frame to hold the entry + button
input_frame = tk.Frame(root)
input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# put the Text box in the output frame and let it expand
output_box = tk.Text(output_frame, bg="black", fg="lime", font=("Courier", 10))
output_box.pack(fill=tk.BOTH, expand=True)

# pack the entry to the left, letting it expand
entry = tk.Entry(input_frame)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry.bind("<Return>", lambda event: handle_command())

# pack the button to the right of the entry
submit_btn = tk.Button(input_frame, text="Submit", command=handle_command)
submit_btn.pack(side=tk.LEFT, padx=(5, 0))

output("Welcome to the Dice Simulator! Type 'HELP' for instructions.")
root.mainloop()
