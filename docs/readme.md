# File Comparator

File Comparator is a simple Python tool designed to compare the contents of two text files and identify unique lines in each file. It's useful for quickly finding differences between two lists or text datasets.

## Features

- Compare two text files line by line.
- Generate output files containing unique lines from each input file.
- Handle sorted text files in lexicographic order.

## Getting Started

These instructions will help you set up and run File Comparator on your local machine.

### Prerequisites

- Python 3.x

### Installation

Clone the repository or download the source code to your local machine. No additional installation is required, as File Comparator uses Python's standard libraries.

### Usage

1. Place your input text files (`input1.txt` and `input2.txt`) in the project directory.
2. Run the script from the command line:

    ```bash
    python src/compare_files.py
    ```

3. Check the output files (`output1.txt` and `output2.txt`) in the same directory for the results.

## Running the Tests

To run the unit tests for File Comparator:

```bash
python -m unittest tests/test_compare_files.py
