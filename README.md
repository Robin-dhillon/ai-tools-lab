# ai-tools-lab
## Project Description

**AI Tools Lab** is a Python project that demonstrates basic sorting algorithms and useful utility functions. The project is designed for learning and practicing Python programming with the help of AI-assisted development tools.

### Features
- Bubble Sort algorithm
- String palindrome checking
- Word counting
- Celsius to Fahrenheit conversion
- Simple and reusable Python modules

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-tools-lab.git
```

2. Navigate to the project directory:

```bash
cd ai-tools-lab
```

3. Make sure Python 3 is installed on your system.

## Usage

### Bubble Sort

```python
from sorting import bubble_sort

numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))
```

**Output:**
```text
[11, 12, 22, 25, 34, 64, 90]
```

### Utility Functions

```python
from utils import is_palindrome, count_words, celsius_to_fahrenheit

print(is_palindrome("madam"))
print(count_words("Python is easy to learn"))
print(celsius_to_fahrenheit(25))
```

**Output:**
```text
True
5
77.0
```

## Project Structure

```text
ai-tools-lab/
│
├── hello.py
├── sorting.py
├── utils.py
└── README.md
```

## Contributors

**Robin Dhillon**

This project was created as part of a practical exercise on GitHub, Git, Python, and AI-assisted development.

## License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project according to the terms of the MIT License.
