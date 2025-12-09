import json
import os
import random
import string

FILE = "urls.json"

def load_data():
    if not os.path.exists(FILE):
        return {}
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def generate_code(n=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(n))

def shorten(url):
    data = load_data()
    for c, u in data.items():
        if u == url:
            return c
    while True:
        code = generate_code()
        if code not in data:
            data[code] = url
            save_data(data)
            return code

def redirect(code):
    data = load_data()
    return data.get(code)

while True:
    print("\nURL Shortener")
    print("1. Shorten URL")
    print("2. Redirect Code")
    print("0. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        url = input("Enter URL: ").strip()
        c = shorten(url)
        print("Short code:", c)

    elif choice == "2":
        code = input("Enter code: ").strip()
        result = redirect(code)
        if result:
            print("Original URL:", result)
        else:
            print("Code not found.")

    elif choice == "0":
        break

    else:
        print("Invalid choice.")


# The URL Shortener program is designed to convert long URLs into short, unique codes and retrieve the original URL using that code. The system replicates the basic behavior of real-world URL shortening services but operates locally using a JSON file as a storage mechanism. The logic implemented emphasizes simplicity, reliability, and persistence of data so that shortened URLs remain available even after the program is closed.

# The program begins by defining a JSON file that acts as its storage database. This file stores key–value pairs where the key is the short code and the value is the full URL. To work with this storage, two foundational functions are used: one for loading existing data and another for saving updated data. When loading, the program checks whether the JSON file exists before attempting to read it. If the file does not exist or an error occurs during reading, the program simply returns an empty dictionary. This ensures that the program always has a valid data structure to work with.

# The next important component is the function that generates unique codes. Each short code is six characters long and consists of randomly chosen letters and digits. This randomness helps reduce the likelihood of collisions, meaning two different URLs receiving the same code. The actual generation uses Python’s built-in random.choice() method to randomly pick characters from a predefined pool consisting of uppercase letters, lowercase letters, and digits. The six-character length provides enough possible combinations to avoid conflicts in typical usage.

# When a user wants to shorten a URL, the program first loads existing mappings from the JSON file. It then checks whether the URL has already been shortened earlier. If it finds a match, it simply returns the existing code, ensuring that the same URL does not receive multiple different codes. If the URL has not been shortened before, the program enters a loop where it generates a new code and verifies that the code is not already used. Once a unique code is found, it is added to the dictionary and stored back into the JSON file. This ensures persistence so that even after restarting the program, the URL–code relationship remains intact.

# The redirect function allows the user to retrieve the original URL by providing a short code. Similar to the shorten function, it begins by loading the JSON data. It then checks if the provided code exists in the dictionary. If found, it returns the corresponding original URL; otherwise, it returns a message indicating that the code does not exist. This simple lookup operation enables fast access, mimicking how a real URL redirection service functions.

# For user interaction, the program includes a small console menu. The user can choose to shorten a URL, look up a URL using a code, or exit the program. This menu loops continuously, allowing multiple operations without restarting. The simple text-based interface ensures usability while keeping the program easy to understand.

# Overall, the logic is straightforward but effective: maintain persistent storage, generate unique codes, avoid duplication, and provide quick lookup for redirection. The design captures the essential behavior of a URL-shortening system in an accessible and easy-to-maintain form.