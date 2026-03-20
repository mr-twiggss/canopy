# canopy
# 📁 Directory Schema Validator

Validate and enforce directory structures using a schema-driven approach with recursive traversal and regex-based matching.

---

## 🚀 Overview

This project provides a lightweight utility to **validate filesystem directory trees against a predefined schema**. It recursively traverses directories and ensures that each file and folder matches expected naming patterns or exact rules.

It is especially useful for:

* Enforcing consistent project structures
* Validating generated datasets or pipelines
* Building tooling similar to linters for filesystems

---

## ⚙️ How It Works

The core idea is simple:

* You define a **schema** using dictionaries, strings, or regex patterns
* The tool **recursively walks the directory tree**
* Each file/folder is **matched against the schema**
* It reports matches and validation errors

---

## 🧠 Key Features

* 🔁 Recursive directory traversal
* 🔍 Regex-based name matching
* 🧩 Flexible schema definition (dict, string, regex)
* 🚫 Ignores hidden/system files (`.DS_Store`, `__MACOSX`, etc.)
* 🧱 Extensible validation logic

---

## 🏗️ Core Functions

### `traverse_dir_tree_with_validations(...)`

Recursively walks through the directory tree and validates each node against the schema.

### `match_iname_with_format(...)`

Dispatcher that routes matching logic based on schema type.

---

## 📦 Example Schema

```python
schema = {
    "src": {
        r".*\.py": None
    },
    "README.md": None,
    r"tests?": {
        r"test_.*\.py": None
    }
}
```

---

## ▶️ Usage

```python
from pathlib import Path

traverse_dir_tree_with_validations(
    item_path=Path("./your_project"),
    format_for_level=schema
)
```

---

## 📌 Output

The script prints:

* Each file/folder encountered
* Whether it matched the schema
* Errors when:

  * No match is found
  * Multiple regex matches occur

---

## 📄 License

MIT (or your preferred license)
