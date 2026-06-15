# Using Python 3.12 for TensorFlow on Windows

## Why?

TensorFlow may not support the newest Python versions immediately. If Python 3.14 is installed, TensorFlow installation can fail with errors such as:

```text
ERROR: No matching distribution found for tensorflow
```

The solution is to create a virtual environment using Python 3.12.

---

## Step 1: Verify Installed Python Versions

Open Command Prompt or PowerShell and run:

```bash
py --list
```

Example output:

```text
-V:3.14 *
-V:3.12
```

This confirms that both Python 3.14 and Python 3.12 are installed.

---

## Step 2: Navigate to the Project Folder

```bash
cd "D:\5. Language Learning\AI ML\Learning-ML-AI"
```

Replace the path with your project directory if different.

---

## Step 3: Create a Virtual Environment Using Python 3.12

```bash
py -3.12 -m venv tf_env
```

This creates a folder named:

```text
tf_env
```

containing an isolated Python 3.12 environment.

---

## Step 4: Activate the Virtual Environment

Command Prompt:

```bash
tf_env\Scripts\activate
```

PowerShell:

```powershell
.\tf_env\Scripts\Activate.ps1
```

When activated, you'll see:

```text
(tf_env) D:\...
```

at the beginning of the terminal prompt.

---

## Step 5: Confirm Python Version

```bash
python --version
```

Expected output:

```text
Python 3.12.x
```

---

## Step 6: Upgrade pip

```bash
python -m pip install --upgrade pip
```

Verify:

```bash
pip --version
```

---

## Step 7: Install TensorFlow

```bash
pip install tensorflow
```

Verify installation:

```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

Example output:

```text
2.xx.x
```

---

## Step 8: Configure VS Code

1. Open the project in VS Code.
2. Press:

```text
Ctrl + Shift + P
```

3. Select:

```text
Python: Select Interpreter
```

4. Choose:

```text
.\tf_env\Scripts\python.exe
```

or the Python 3.12 interpreter.

---

## Step 9: Verify in VS Code

Open a terminal in VS Code:

```bash
python --version
```

Expected:

```text
Python 3.12.x
```

---

## Step 10: Install ML Libraries

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

Optional:

```bash
pip install tensorflow keras
```

---

## Useful Commands

Check Python version:

```bash
python --version
```

List installed packages:

```bash
pip list
```

Deactivate environment:

```bash
deactivate
```

Delete environment:

```bash
rmdir /s tf_env
```

(Recreate it later with Step 3.)

---

## Running Scripts

Instead of:

```bash
python decision_tree.py
```

activate the environment first:

```bash
tf_env\Scripts\activate
python decision_tree.py
```

This ensures TensorFlow and all ML packages use Python 3.12.

---

## Recommended Workflow

For every machine learning project:

1. Create a dedicated virtual environment.
2. Install project-specific packages.
3. Select the environment in VS Code.
4. Never install TensorFlow into the global Python installation.
5. Keep Python 3.14 for other projects and Python 3.12 for TensorFlow projects.

```
```
