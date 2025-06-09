# Level Up Your CLI: Building a Simple Skincare Autocomplete in Python

![Demo animation](demo.gif)

## Why Autocomplete?

Searching long lists can be tedious. Autocomplete speeds up the process by
suggesting options as you type. In this project I built a small tool that helps
users explore skincare categories using a command line interface.

## How It Works

The program stores category data in a Python dictionary and precomputes a sorted
list of category names. To efficiently find matches, it performs a binary search
with the `bisect` module instead of scanning every entry. Each category includes
sample products and a short description that are displayed when selected.

```bash
python3 Skincarerecommendation.py
```

Type a prefix to see matching categories and then pick one to view details.

The full source code is [on GitHub](https://github.com/example/SkinCare-Recommendation-System).

## Conclusion

Although lightweight, this demo shows how data structures and algorithms impact
user experience. A small change from linear search to binary search makes the
autocomplete snappy even as the data set grows. Try extending the script with
more categories or product data to see how it scales!
