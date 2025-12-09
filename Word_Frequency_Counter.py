from typing import Dict
import re

def word_frequency_counter(text: str) -> Dict[str, int]:
    cleaned = re.sub(r"[^\w\s]", " ", text)
    words = [w.lower() for w in cleaned.split() if w.strip()]
    
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    return dict(sorted(freq.items(), key=lambda x: (-x[1], x[0])))

if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")

    result = word_frequency_counter(paragraph)

    print("\nWord Frequencies:\n")
    for word, count in result.items():
        print(f"{word} - {count}")

# The Word Frequency Counter program is designed to analyze a paragraph of text entered by the user and determine how many times each unique word appears. The main goal of the logic is to process the text in a clean, structured way so that words are counted accurately, regardless of punctuation, spacing, or letter casing. The implementation focuses on simplicity, efficiency, and accuracy.

# The first step in the program is to accept user input. The user is prompted to enter a paragraph, which may contain uppercase letters, lowercase letters, punctuation marks, symbols, or multiple spaces. This raw input cannot be processed reliably without cleaning, so the next major step involves text preprocessing. The program uses a regular expression to remove all punctuation and unwanted characters. This is done with the help of Python’s re module, specifically by replacing anything that is not a word character or whitespace with a blank space. This ensures that words like “hello,” and “hello” are treated the same once punctuation is removed.

# After cleaning, the program splits the paragraph into individual words. The split() method is used because it automatically separates the text based on whitespace. To ensure consistency, every word is converted to lowercase. This avoids treating “Hello” and “hello” as different words. The logic then filters out empty strings that might appear during splitting.

# Next comes the frequency counting stage. A dictionary is used because it provides an efficient way to map unique words to their counts. The program iterates through each word and checks whether it is already present in the dictionary. If it is, the count is increased by one. If not, the word is added with an initial count of one. This simple but effective mechanism ensures that every unique word is captured.

# Once all words have been processed, the dictionary contains the full frequency distribution. However, to make the output more meaningful, the program sorts the results. The sorting is done on two levels: first, by frequency in descending order and second, alphabetically for words that share the same frequency. This is achieved using Python’s sorted() function with a custom lambda function, which provides precise control over sorting behavior. Sorting helps present the data in a readable and organized manner, making it easy for users to identify the most frequently used words.

# Finally, the results are displayed to the user. Each word is printed along with its corresponding count in a simple and clear format. This completes the logical flow of the program: input → cleaning → splitting → normalization → counting → sorting → output.

# Overall, the Word Frequency Counter demonstrates essential programming concepts such as string manipulation, regular expressions, dictionaries, sorting with custom keys, and user interaction. Its modular approach ensures accuracy while remaining easy to understand and extend. The logic can be adapted for larger text analysis tasks, making it a practical foundation for more advanced natural language processing applications.