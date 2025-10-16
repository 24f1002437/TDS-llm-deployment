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
---
title: Odd Even API
colorFrom: red
colorTo: yellow
sdk: docker
pinned: false
license: mit
short_description: Flask app for the TDS LLM Deployment project
---

#  Odd/Even Number Classifier

A simple **Flask API** that classifies numbers as **odd** or **even**, built as part of the **TDS LLM Deployment Project**.

---

## 🚀 Live Deployment

👉 **Hugging Face Space:** [ms3011/odd-even-api](https://huggingface.co/spaces/ms3011/odd-even-api)

### API Endpoint: https://ms3011-odd-even-api.hf.space/api


### Example Request (via `curl`)
```bash
curl -X POST "https://ms3011-odd-even-api.hf.space/api" \
-H "Content-Type: application/json" \
-d "{\"secret\":\"(given)\",\"numbers\":[1,2,3,4,5]}"



## License

This project is licensed under the MIT License.
