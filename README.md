# Smartphone Data Analysis: Professional Code Review

This repository contains my solution to the DataCamp "Performing a Code Review" project. 

## 📋 Project Background
Acting as a **Senior Data Scientist**, I performed a comprehensive code review on a workflow designed for a university procurement team. I refactored a Junior Developer's codebase to ensure it was production-ready, modular, and followed industry best practices.

---

## 🚀 Technical Refactor Summary
This project involved a comprehensive code review and refactoring of a smartphone data cleaning and visualization workflow. The primary goal was to transition "Junior" level code into a production-ready, maintainable, and well-tested Python module.

### 🛠️ Key Improvements & Engineering Decisions
1. **Data Integrity & Memory Management**
* **Resolved** `SettingWithCopyWarning`: Identified and fixed a common Pandas slice-assignment risk by implementing explicit `.copy()` on filtered DataFrames.
* **Standardized Units**: Standardized the `price` column by converting values from cents to dollars for intuitive visualization.  

2. **Clean Code & PEP-8 Standards**
* **Naming Conventions**: Refactored the entire codebase from `camelCase` to `snake_case` to align with PEP-8 style guidelines.
* **DRY (Don't Repeat Yourself)**: Eliminated duplicated string manipulation logic by centralizing label formatting within a dedicated `column_to_label` helper function.

3. **Professional Documentation**
* **Stale Docstring Correction**: Identified and corrected a "documentation drift" where the docstring incorrectly described a pattern between `avg_rating` and `battery_capacity` while the actual logic compared variables against `price`.
* **Standardized Formatting**: Updated all docstrings to follow the PEP-257 imperative style, including `:param` and `:return` definitions.

4. **Testing & Reliability**
* **Logic Bug Fix**: Caught and corrected a "double-negative" logic error in the unit tests that was causing valid data to fail assertions.
* **Migration to Pytest**: Decoupled the testing logic from `ipytest` (notebook-based) to a standard `pytest` suite, making the project compatible with modern CI/CD pipelines.
* **Module Protection**: Implemented an `if __name__ == "__main__":` block to protect the visualization logic, preventing unintended GUI pop-ups during automated testing runs.

### 🧪 Environment & Tools
* **Language**: Python 3.8+
* **Libraries**: Pandas, Seaborn, Matplotlib
* **Testing**: Pytest
* **Config**: Managed via pyproject.toml and .gitignore

---

## 📁 Repository Structure
* `src/smartphone_utils.py`: Contains the refactored data cleaning and visualization functions.
* `tests/test_smartphones.py`: Standardized Pytest suite for data validation.
* `data/smartphones.csv`: The raw dataset used for the analysis.
* `pyproject.toml`: Project configuration and dependency management.

## ⚙️ How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`
4. Run the script: `python src/smartphone_utils.py`