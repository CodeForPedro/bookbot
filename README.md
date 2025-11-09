# bookbot
BookBot is my first [Boot.dev](https://www.boot.dev) project! It's a simple command-line tool that analyzes text files (such as books) to show:

- The total word count.
- The frequency of each alphabetical character.

It’s great for exploring text statistics and practicing Python file and text handling.

---

## Requirements

- Python 3.10+
- A plain text file

---

## Usage

1. Clone or download this repository.  
2. Open your terminal and navigate to the root project directory.  
3. Run the program with: python3 main.py <path_to_book>

---

## Example
Input:
    python3 main.py books/frankenstein.txt

Output:
    ============ BOOKBOT ============
    Analyzing book found at books/mobydick.txt...
    ----------- Word Count ----------
    Found 215838 total words
    --------- Character Count -------
    e: 119354
    t: 89875
    a: 79224
    ...
    ============= END ===============