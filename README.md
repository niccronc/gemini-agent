# 🛠️ Embodying Gemini with agentic capabilities

This project embodies an LLM with agentic capabilities, and allows a user to interact with through the terminal.

Last updated: June 15, 2025.

---

## 💡 Ideation

This small PoC was born after reading [this](https://ampcode.com/how-to-build-an-agent) excellent article on AmpCode.
Since Anthropic does not offer a free tier compatible with their SDK, I decided to reframe my implementation to use Gemini.

The result is even more stark: our agentic model (Gemini, imbibed with file management capabilities) is implemented in less than 200 lines of Python code.
The two main reasons for the even simpler code are:
1. Python's syntax is simpler and shorter than Go, and still suffices for this small example.
2. Gemini's tools capabilities (for the Python SDK) allow the model to directly interact with the result of a function call, without requiring our script to parse the response and feed it back to the model.

---

## 📁 Project Structure

```text
.
├── main.py                     # Main interactive script
├── README.md                   # Documentation
├── requirements.txt            # Requirements
└── tools/
    ├── __init__.py               # Makes tools a package
    └── file_system_management.py # Helper functions for file operations
```

---

## 🛠️ Setup and Run Instructions

Follow these steps to get the interactive chat script up and running:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/niccronc/gemini-agent.git
    cd gemini-agent
    ```

2. **Ensure you have Python installed**:

    - The script requires **Python 3.10 or higher**.
    - Check your Python version by running:

      ```bash
      python --version
      ```

3. **(Optional but highly recommended) Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Get a Gemini API key**:

    - Follow the instructions [here](https://ai.google.dev/gemini-api/docs/api-key) to get a Gemini API key.
    - Store your API key somewhere safe, and never share it with anyone.
    - Create a `GEMINI_API_KEY` environment variable in your virtual environment, and set it equal to your API key:

      ```bash
      export GEMINI_API_KEY='<your api key>'
      ```


5. **Run the script from the terminal**:

    ```bash
    python script.py --name <your name>
    ```

6. **Interact with the script**:

    - The agent will greet you.
    - Type commands or messages and press **Enter**.
    - To exit the session, type `\exit` and press **Enter**.

---

## 🧩 Current Capabilities & WIP Features

### ✅ Implemented Features

- Interactive chat session in the terminal
- Navigate the file system (listing files, copy and moving files, creating files)
- Overwrite protection: prevents accidental file loss

### 🛠️ Work in Progress (WIP)

- Delete functionality with safety checks
- Command logging/history

---

## 🔁 Fully Worked Example

Let's walk through an example.
We will ask Gemini to create an executable python script that finds and writes to stdout the first N prime numbers.

```bash
$ python script.py --name Nico

> Hello Nico! How can I help you?
> Type \exit to leave the chat.

> You: write to file a python script finding the first N prime numbes and outputting them to screen. N should be an argument of the script.
> Gemini: Could you please specify the file path where you want to save the Python script?

> You: primes.py
> Gemini: I have created a file named `primes.py` with the Python script to find the first N prime numbers and output them to the screen. The script takes N as a command-line argument.

> You: is there a default value for the parameter, or is it a required parameter?
> Gemini: The script does not have a default value for the parameter N. It is a required parameter. If you run the script without providing a value for N, it will print a message asking you to provide the argument.

> You: update the script to use N=10 as a default value
> Gemini: I have updated the `primes.py` script to use a default value of N=10 if no command-line argument is provided.

> You: what command should i use from terminal to execute the script?
> Gemini: To execute the script from the terminal, you would use the command `python primes.py`. If you want to specify a value for N other than the default (10), you can include it as a command-line argument like this: `python primes.py 20`.

> You: \exit
> Goodbye!
```

The resulting script:
```python
import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            if n <= 0:
                print("Please enter a positive integer.")
                sys.exit(1)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            sys.exit(1)
    else:
        n = 10  # Default value

    prime_numbers = find_primes(n)
    print(prime_numbers)
```