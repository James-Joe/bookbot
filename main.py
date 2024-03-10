def get_book(path:str) -> str:
    """returns the book as a string"""
    with open(path) as f:
        file_contents = f.read()
    return file_contents
    
def word_count(book:str) -> int:
    """Return word count of book"""
    words = book.split()
    return len(words)

def count_letters(book:str) -> dict:
    """Count the number of occurrences for
        each letter of the alphabet"""
    lst = []
    dic = {}
    lower_text = book.lower()
    for word in lower_text:
        for letter in word:
            if not letter.isalpha():
                continue
            if letter not in dic:
                dic[letter] = 1
            if letter in dic:
                dic[letter] += 1
    for key, val in dic.items():
        lst.append({key:val})
    return lst

def gen_report(file:str) -> str:
    """Generate a report"""
    count = word_count(file)
    letter_count = count_letters(file)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in this document")
    for i in letter_count:
        for key, val in i.items():
            print(f"The character {key} appears {val} times")
        
    


def main():
    file = get_book("./books/frankenstein.txt")
    print(gen_report(file))
if __name__ == "__main__":
    main()