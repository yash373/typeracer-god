# Typeracer God

Typeracer God is an automated Python program designed to give you an edge in Typeracer games. The bot automatically types the text for you in a race after you copy the race text from the browser. Simply copy the text, run the bot, and press the hotkey (`Ctrl + Alt + I`) to start winning races!

## Features

- **Automated typing:** Quickly type the copied text during a race, allowing you to win effortlessly.
- **Hotkey activation:** The program is activated using the `Ctrl + Alt + I` keyboard shortcut.
- **Python-based solution:** The entire bot is built using Python, making it easy to customize and extend.

## Requirements

- **Python 3.x** installed on your machine.
- A **browser extension** or method that allows you to easily copy all the race text in Typeracer.
    - Example extensions: [Copyfish](https://chrome.google.com/webstore/detail/copyfish-free-ocr-softwar/ocdlmjhbenodhlknglojajgokahaglga) or [Enable Copy](https://chrome.google.com/webstore/detail/enable-copy/nkbihfbeogaeaoehlefnkodbefgpgknn) for Chrome/Firefox.
- **Keyboard**: Program activates the typing bot using the keyboard shortcut `Ctrl + Alt + I`.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yash373/typeracer-god.git
    cd typeracer-bot
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Install a browser extension that allows you to copy all text from the race window. Example: "Enable Copy" or "Copyfish OCR" (check the links above).

## Usage

1. Open Typeracer in your web browser and start a race.
2. Use your browser extension to copy all the race text from the race window.
3. Run the Python script:
    ```bash
    python main.py
    ```
4. Select the typing textbox in Typeracer.
5. Press `Ctrl + Alt + I` to activate the bot. The bot will automatically start typing the text in the race, ensuring a win!

## Hotkey

- **Ctrl + Alt + I**: Starts the bot and initiates typing the copied text into the Typeracer text field.

## Important Notes

- The bot depends on you copying the race text before it can type. Make sure to copy the text using a browser extension before starting the program.
- The bot types at a human-like speed to avoid detection. However, use it responsibly as using bots in online games might violate terms of service.

## Contributing

If you'd like to contribute or improve the bot, feel free to fork the project and submit a pull request.

## License

This project is licensed under the MIT License.
