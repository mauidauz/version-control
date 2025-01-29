from datetime import datetime

# Get current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md
with open("version.md", "w") as file:
    file.write(f"Last updated: {current_time}\n")

print("version.md updated successfully!")
