# Odd/Even Number Classifier

A simple Python module to classify numbers as odd or even.

## How to run tests

To run the tests, you need to have pytest installed:

```bash
pip install pytest
```

Then, you can run the tests from the root of the repository:

```bash
pytest
```

## Example usage

```python
from odd_even import classify_numbers

numbers = [1, 2, 3, 4, 5, 6]
result = classify_numbers(numbers)
print(result)
# Output: ['odd', 'even', 'odd', 'even', 'odd', 'even']
```

## License

This project is licensed under the MIT License.
