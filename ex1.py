def save_text_to_file(filename, text):
    """
    Save the given text to a file.

    Args:
        filename (str): The name of the file to save the text to.
        text (str): The text to save in the file.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:  # Changed to append mode
            file.write(text + '\n')  # Add a newline after each text input
        print(f"Text successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    filename = input("Enter the filename (with extension): ")
    print("Start entering text. Type 'exit' to finish.")
    while True:
        text = input("Enter the text to save: ")
        if text.lower() == 'exit':
            print("Exiting and saving text.")
            break
        save_text_to_file(filename, text)
