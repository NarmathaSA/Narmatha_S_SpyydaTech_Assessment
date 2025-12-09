BRACKET_PAIRS = {')': '(', ']': '[', '}': '{'}

def is_balanced_brackets(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != BRACKET_PAIRS[ch]:
                return False
            stack.pop()
    return len(stack) == 0

user_input = input("Enter a bracket string: ")
result = is_balanced_brackets(user_input)
print("Balanced?", result)


# The Balanced Brackets Validator is a program designed to determine whether a given string of brackets is properly balanced. Brackets are considered balanced when every opening bracket has a corresponding closing bracket in the correct order. This type of validation is widely used in programming language compilers, mathematical expression checking, and syntax validation tools. The core logic of this program revolves around the use of a stack data structure, which provides an efficient and intuitive mechanism for handling nested and sequential bracket patterns.

# The program begins by defining a mapping between closing brackets and their corresponding opening brackets. This mapping includes three types of brackets: parentheses (), square brackets [], and curly braces {}. By creating this dictionary, the program can quickly identify which type of opening bracket is expected for any encountered closing bracket. This step is essential because each closing bracket must match the correct type of opening bracket for the expression to be valid.

# The primary function iterates through each character in the input string. For every character, the logic checks whether it is an opening bracket. If it is, the program pushes the bracket onto a stack. A stack is the ideal structure for this purpose because it operates on the Last-In-First-Out (LIFO) principle, meaning the most recently encountered opening bracket is the first one that must be matched. This aligns perfectly with the rules of balanced brackets, especially in nested expressions.

# When the program encounters a closing bracket, it performs two crucial checks. First, it verifies whether the stack is empty. If the stack is empty at this point, it means there is a closing bracket without a preceding opening bracket, making the expression unbalanced. Second, if the stack is not empty, the program compares the top element of the stack with the expected opening bracket for the encountered closing bracket. If they do not match, it indicates incorrect pairing, and the function immediately returns false.

# If the brackets match correctly, the opening bracket is removed from the stack, meaning that particular pair has been successfully validated. The program continues scanning the remaining characters in the string. This systematic push-pop mechanism ensures that the nesting structure is respected and that brackets close in the correct order.

# After processing all characters, the final step is to check whether the stack is empty. A non-empty stack means there are unmatched opening brackets remaining, which indicates an incomplete or unbalanced expression. If the stack is empty, it means that all brackets were properly matched and the input string is balanced.

# Overall, the logic implemented is efficient, elegant, and widely used in real-world applications. It handles simple sequences, deeply nested structures, and incorrect bracket combinations with equal effectiveness. By using a stack-based approach, the algorithm maintains optimal time complexity while ensuring accurate validation of even complex expressions.