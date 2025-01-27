import requests
from bs4 import BeautifulSoup

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []
        print("TextEditor initialized")

    def insert_text(self, text, position):
        print(f"Inserting text at position {position}: '{text}'")
        self.undo_stack.append(("delete", text, position))
        self.text = self.text[:position] + text + self.text[position:]
        self.redo_stack.clear()
        print(f"Text after insertion: {self.text}")

    def delete_text(self, start, end):
        print(f"Deleting text from position {start} to {end}")
        deleted_text = self.text[start:end]
        self.undo_stack.append(("insert", deleted_text, start))
        self.text = self.text[:start] + self.text[end:]
        self.redo_stack.clear()
        print(f"Text after deletion: {self.text}")

    def import_from_file(self, filename):
        print(f"Importing content from file: {filename}")
        try:
            with open(filename, "r") as file:
                imported_text = file.read()
                self.undo_stack.append(("import", self.text))
                self.text += "\n" + imported_text
            print(f"Content from {filename} imported")
            self.redo_stack.clear()
        except FileNotFoundError:
            print(f"File not found: {filename}")

    def import_from_url(self, url):
        print(f"Importing content from URL: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            imported_text = soup.get_text()

            self.undo_stack.append(("import", self.text))
            self.text += "\n" + imported_text
            print("Content imported from URL")
            self.redo_stack.clear()

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch content from URL: {e}")

    def undo(self):
        print("Undo operation")
        if self.undo_stack:
            action = self.undo_stack.pop()
            if action[0] == "insert":
                self.text = self.text[:action[2]] + action[1] + self.text[action[2]:]
            elif action[0] == "delete":
                self.text = self.text[:action[2]] + self.text[action[2] + len(action[1]):]
            self.redo_stack.append(action)
            print(f"Text after undo: {self.text}")
        else:
            print("Nothing to undo")

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            if action[0] == "insert":
                self.text = self.text[:action[2]] + self.text[action[2] + len(action[1]):]
            elif action[0] == "delete":
                self.text = self.text[:action[2]] + action[1] + self.text[action[2]:]
            self.undo_stack.append(action)
            self.view_text()
            print(self.text)


    def view_text(self):
        print("Viewing current text")
        return self.text

    def clear_text(self):
        print("Clearing text")
        self.undo_stack.append(("clear", self.text))
        self.text = ""
        self.redo_stack.clear()

    def find_and_replace(self, find_text, replace_text):
        print(f"Find and replace: '{find_text}' with '{replace_text}'")
        self.undo_stack.append(("replace", find_text, replace_text, self.text))
        self.text = self.text.replace(find_text, replace_text)
        self.redo_stack.clear()
        print(f"Text after replace: {self.text}")

    def replace_all(self, find_text, replace_text):
        print(f"Replace all occurrences of '{find_text}' with '{replace_text}'")
        self.undo_stack.append(("replace", find_text, replace_text, self.text))
        count = self.text.count(find_text)
        self.text = self.text.replace(find_text, replace_text)
        self.redo_stack.clear()
        print(f"Replaced {count} occurrences of '{find_text}' with '{replace_text}'.")
        print(f"Text after replacing all: {self.text}")

    def save_file(self, filename):
        print(f"Saving text to file: {filename}")
        with open(filename, "w") as file:
            file.write(self.text)
        print(f"File saved as {filename}")

    def open_file(self, filename):
        print(f"Opening file: {filename}")
        try:
            with open(filename, "r") as file:
                self.undo_stack.append(("open", self.text))
                self.text = file.read()
            print(f"File {filename} opened")
            self.redo_stack.clear()
        except FileNotFoundError:
            print(f"File not found: {filename}")

    def word_count(self):
        return len(self.text.split())

def main():
    editor = TextEditor()

    while True:
        print("\nText Editor Menu:")
        print("1. Insert Text")
        print("2. Delete Text")
        print("3. Undo")
        print("4. Redo")
        print("5. View Text")
        print("6. Clear Text")
        print("7. Find and Replace")
        print("8. Replace All")
        print("9. Save File")
        print("10. Open File")
        print("11. Word Count")
        print("12. Import from Another File")
        print("13. Import from URL")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter text to insert: ")
            position = int(input("Enter position to insert: "))
            editor.insert_text(text, position)
        elif choice == "2":
            start = int(input("Enter start position to delete: "))
            end = int(input("Enter end position to delete: "))
            editor.delete_text(start, end)
        elif choice == "3":
            editor.undo()
        elif choice == "4":
            editor.redo()
        elif choice == "5":
            print(editor.view_text())
        elif choice == "6":
            editor.clear_text()
        elif choice == "7":
            find_text = input("Enter text to find: ")
            replace_text = input("Enter text to replace with: ")
            editor.find_and_replace(find_text, replace_text)
        elif choice == "8":
            find_text = input("Enter text to find: ")
            replace_text = input("Enter text to replace with: ")
            editor.replace_all(find_text, replace_text)
        elif choice == "9":
            filename = input("Enter filename to save: ")
            editor.save_file(filename)
        elif choice == "10":
            filename = input("Enter filename to open: ")
            editor.open_file(filename)
        elif choice == "11":
            print("Word count:", editor.word_count())
        elif choice == "12":
            filename = input("Enter filename to import: ")
            editor.import_from_file(filename)
        elif choice == "13":
            url = input("Enter URL to import text from: ")
            editor.import_from_url(url)
        elif choice == "14":
            print("Exiting the editor.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
