def count_words(text: str):
    words = text.split()
    return len(words)

def count_each_letter(text: str):
    text = text.lower()
    letters: dict[str, int] = {}
    for char in text:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

def sort_on(items):
    return items["num"]

def sort_table(table: dict[str, int], reverse: bool = False):
    sorted_table = []
    for char, num in table.items():
        sorted_table.append({"char": char, "num": num})
    sorted_table.sort(key=sort_on, reverse=reverse)
    return sorted_table
