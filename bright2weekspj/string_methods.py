text = input("Enter a sentence: ")

print("\n---- Cleaned Versions ----")
print("1. UPPERCASE:", text.upper())
print("2. lower case:", text.lower())
print("3. Title case.", text.title())
print("4. Remove extra spaces:", " ".join(text.split()))
print("5. Replace 'a' with @:", text.replace("a", "@"))
print("6. Word Count:", len(text.split()))