# This script asks the user for a filename and handles errors gracefully

filename = input("📄 Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("✅ File content:")
        print(content)

except FileNotFoundError:
    print("❌ File not found. Please check the filename and try again.")
except PermissionError:
    print("🚫 You don't have permission to read this file.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
