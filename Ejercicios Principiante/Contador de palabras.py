def word_counter():
    # 1. Prompt the user for input text
    text_input = input("Enter the text or paragraph you want to analyze: ").strip()

    if not text_input:
        print("You did not enter any text.")
        return
    
    # 2. Split the text into word using spaces as delimiters
    # The .split() method handles multiple spaces automatically
    word_list = text_input.split()

    # 3. Count the number of elements in the list
    word_count = len(word_list)

    # 4. Calculate additional statistics (opcional but useful)
    char_count = len(text_input)

    # 5. Display the results
    print("\nAnalysis Results:")
    print(f"Total of words: {word_count}")
    print(f"Total of characters: {char_count}")

if __name__ == "__main__":
    word_counter()