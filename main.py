file_path = 'books/frankenstein.txt'
with open(file_path) as f:
    book = f.read()
    words = book.split()

    characters = {}
    for character in book.lower():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    
    # print(characters)

    print(f"The book contains {len(words)} words")
    print(f"{len(words)} words found in the document")

    for character, count in characters.items():
        if (character == " "):
            print(f"The space character was found {count} times")
        elif (character == "\n"):
            print(f"The new line character was found {count} times")
        elif (character == "\x0c"):
            print(f"The form feed character was found {count} times")
        elif (character == "\x18"):
            print(f"The cancel character was found {count} times")
        else:
            print(f"The {character} character was found {count} times")

