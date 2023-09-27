### Transcriptify

Transcriptify is a simple Python web application that adds transcript tags to text input. It allows you to insert "{Transcript Start}" at the beginning of the text, "{Transcript Continues}" every 4000 characters within a sentence, and "{Transcript End}" at the end of the text.

Features
- Add "{Transcript Start}" at the beginning of the input text.
- Insert "{Transcript Continues}" every 4000 characters within a sentence.
- Add "{Transcript End}" at the end of the input text.

Usage
1. Install the required packages using pip:
    ```bash
    pip install gradio
    ```
2. Run the application:
    ```bash
    python transcriptify.py
    ```
3. Access the web interface in your web browser at http://localhost:7860.
4. Enter the text in the input textbox and click "Submit." The modified text with transcript tags will be displayed in the output textbox.