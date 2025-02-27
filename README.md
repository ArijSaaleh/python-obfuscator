# Python Code Obfuscator and Deobfuscator

## Project Overview

This Python tool allows you to obfuscate Python scripts by renaming variables and functions into randomized or meaningless names, adding a layer of complexity and protection for intellectual property. The tool can also reverse the obfuscation process using a saved mapping.

### Features:
- **Obfuscation**: Changes the variable and function names to obscure symbols.
- **Deobfuscation**: Restores the obfuscated code to its original form using the saved mapping.
- **Configurable via Command Line**: Choose between obfuscation or deobfuscation directly from the command line.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone <repo-url>
    cd python-obfuscator
    ```

2. Create a virtual environment and activate it:
    - On **Windows**:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    - On **macOS/Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Install the necessary dependencies:
    ```bash
    pip install astunparse
    ```

## Usage

You can obfuscate and deobfuscate Python files using this tool.

### Obfuscating a Python Script:

1. Run the following command to obfuscate a Python file:
    ```bash
    python obfuscator.py obfuscate <your-python-file.py>
    ```

2. After obfuscation, the tool will print the obfuscated code to the console. It will also save a `mapping.json` file that stores the mapping between the original and obfuscated variable/function names.

### Deobfuscating an Obfuscated Script:

1. To deobfuscate the script, use the command:
    ```bash
    python obfuscator.py deobfuscate <your-obfuscated-file.py>
    ```

2. The tool will use the `mapping.json` file to restore the original names.

### Example

#### Original Python Script (`script.py`):
```python
def greet():
    message = "Hello, world!"
    print(message)

greet()
```
### Obfuscating
```bash
    python obfuscator.py obfuscate script.py
```
### Deobfuscating
```bash
    python obfuscator.py deobfuscate obfuscated_script.py
```
### License
This project is open-source and available under the MIT License.