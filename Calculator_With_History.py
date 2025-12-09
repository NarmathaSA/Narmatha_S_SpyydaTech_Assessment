import json
import os

FILE = "history.json"

def load_history():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_history(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def calculate(expr):
    try:
        result = eval(expr, {"__builtins__": None}, {})
        return result
    except:
        return None

def add_to_history(expr, result):
    data = load_history()
    data.append({"expression": expr, "result": result})
    save_history(data)

def get_history():
    return load_history()

while True:
    print("\nCalculator")
    print("1. Calculate")
    print("2. View History")
    print("0. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        expr = input("Enter expression: ")
        res = calculate(expr)
        if res is None:
            print("Invalid expression.")
        else:
            print("Result:", res)
            add_to_history(expr, res)

    elif choice == "2":
        hist = get_history()
        if not hist:
            print("History is empty.")
        else:
            for i, h in enumerate(hist, 1):
                print(f"{i}. {h['expression']} = {h['result']}")

    elif choice == "0":
        break
    else:
        print("Invalid option.")


# The Calculator with History program is designed to perform basic arithmetic operations while maintaining a record of every calculation the user performs. The core purpose of the program is not only to compute results but also to store each expression along with its output so that the user can revisit previous calculations whenever needed. The logic implemented is straightforward, practical, and resembles how a simple real-world calculator with memory functionality might operate.

# The program starts by defining a file, history.json, used to store the calculation history permanently. JSON is chosen because it is lightweight, easy to read, and simple to load into Python structures. Two essential functions manage the history: one loads existing history from the file, and the other saves new history entries. When the program loads history, it checks whether the file exists; if not, it returns an empty list. This ensures that the calculator always has a valid history structure, even on the first run.

# The main calculation is handled through a function that accepts an arithmetic expression from the user and evaluates it using Python’s built-in eval. To prevent unsafe execution, the program restricts eval by removing access to built-in functions. This allows only standard arithmetic operations such as addition, subtraction, multiplication, and division. If the expression is valid, the result is returned; otherwise, the function signals an error by returning None.

# Once a calculation is successful, the program records it. A helper function loads the existing history, appends a new dictionary containing both the expression and the result, and then saves this updated list back to the file. This approach ensures that no calculation is lost and the full history remains intact across sessions. Any time the user wants to view past activity, the program retrieves the entire history list and prints each entry in a readable format.

# The user interface is a simple text-based menu that runs in a loop. This design allows users to perform multiple calculations, view their history, or exit the program. When the user selects the calculation option, the program prompts them for an arithmetic expression. When the user selects the history option, the program displays all previous expressions and their results in a numbered list. This makes it easy to track past calculations and verify accuracy.

# The logic focuses on clarity and usability rather than complexity. It avoids unnecessary features, sticking strictly to the core functions of a calculator: evaluating expressions and storing results. The use of JSON for persistence and the looping menu structure makes the application feel interactive and purposeful. Even though the implementation is simple, it effectively demonstrates file handling, dynamic user input, data storage, and basic expression evaluation.

# Overall, the program delivers a clean and practical solution for a calculator with history tracking. The logic is easy to follow, behaves predictably, and can be expanded with more features if needed.