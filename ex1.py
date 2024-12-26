def save_text_to_file(filename, text):
    """
    Save the given text to a file.

    Args:
        filename (str): The name of the file to save the text to.
        text (str): The text to save in the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    filename = input("Enter the filename (with extension): ")
    text = input("Enter the text to save: ")
    save_text_to_file(filename, text)
