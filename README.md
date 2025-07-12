# BookBot 📚

A simple Python tool that analyzes text files and generates reading statistics reports.

## Features

- **Word Count**: Counts the total number of words in a document
- **Character Frequency**: Analyzes and ranks alphabetic characters by frequency
- **Clean Output**: Generates a formatted report with clear statistics

## Installation

1. Clone or download the project files
2. Ensure you have Python 3.x installed
3. No additional dependencies required - uses only Python standard library

## Usage

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

### Sample Output

```
--- Begin report of books/frankenstein.txt ---

77986 words found in the document

e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
h: 19725
r: 18557
d: 16863

--- End report ---
```

## Project Structure

```
bookbot/
├── main.py          # Main entry point and CLI interface
├── stats.py         # Text analysis functions
└── README.md        # This file
```

## How It Works

1. **main.py**: Handles command-line arguments and orchestrates the analysis
2. **stats.py**: Contains the core logic for:
   - Reading and processing text files
   - Counting words
   - Analyzing character frequency
   - Sorting and displaying results

## Requirements

- Python 3.x
- Text file to analyze (any `.txt` file)

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional text statistics
- Support for different file formats
- Enhanced error handling
- Performance optimizations

