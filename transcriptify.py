import gradio as gr
import re

def add_transcript_tags(input_text):
    # Split input_text into sentences
    sentences = re.split(r'(?<=[.!?])\s', input_text)

    # Initialize the output text
    output_text = "{Transcript Start}\n\n"

    char_count = 0  # Initialize character count

    for sentence in sentences:
        # Check if adding the current sentence exceeds 4000 characters
        if char_count + len(sentence) + len("\n\n{Transcript Continues}\n\n") > 4000:
            output_text += "\n\n{Transcript Continues}\n\n"
            char_count = 0  # Reset character count

        output_text += f"{sentence} "
        char_count += len(sentence) + 1  # Account for space after each sentence

    # Add the Transcript End tag
    output_text += "\n\n{Transcript End}"
    
    return output_text

# Create a Gradio interface
input_text = gr.Textbox()
output_text = gr.Textbox()

iface = gr.Interface(fn=add_transcript_tags, inputs=input_text, outputs=output_text, live=True, capture_session=True)

# Start the Gradio interface
iface.launch()
