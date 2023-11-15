text = input("Enter text: ")
unique_chars = set()

for char in text:
    unique_chars.add(char)

for char in sorted(unique_chars):
    count = text.count(char)
    print(f"{char}: {count} time/s")
