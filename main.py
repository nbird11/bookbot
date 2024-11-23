def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()

    letters = {}
    for char in contents:
        char = char.lower()
        letters[char] = letters.get(char, 0) + 1

    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{len(contents.split())} words found in the document")
    for letter, count in sorted_letters:
        print(f"The {letter!r} character was found {count} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
