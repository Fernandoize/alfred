import json
import pyperclip

def main():
    try:
        # Read JSON data from clipboard
        json_data = pyperclip.paste()

        # Parse JSON data
        parsed_data = json.loads(json_data)

        # Format JSON data
        formatted_data = json.dumps(parsed_data, indent=4)

        # Print formatted data
        print(formatted_data)

        pyperclip.copy(formatted_data)

    except json.JSONDecodeError:
        # Print error message if JSON format is incorrect
        print("Error: Invalid JSON format")

if __name__ == "__main__":
    main()
