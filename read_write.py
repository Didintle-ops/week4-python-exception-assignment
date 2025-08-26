# This script reads from 'input.txt', modifies the content, and writes it to 'output.txt'

def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

try:
    with open("input.txt", "r") as infile:
        original = infile.read()
        modified = modify_content(original)

    with open("output.txt", "w") as outfile:
        outfile.write(modified)

    print("✅ File has been read and modified successfully!")

except FileNotFoundError:
    print("❌ 'input.txt' not found. Please make sure the file exists.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
