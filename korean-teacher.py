from ollama import ChatResponse, chat
from transformers import VitsModel, AutoTokenizer
import torch
import uroman as ur
import sounddevice as sd

prompt = 'You are a Korean teacher. Speak a Korean sentence. And then ask me what it means.'
llmModelName = 'qwen2.5'

ttsModel = VitsModel.from_pretrained("facebook/mms-tts-kor")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-kor")
uroman = ur.Uroman()


def speak_korean(text: str) -> str:
    """
    speak korean text so user can hear it

    Args:
        text (str): text written in hangeul to speak

    Returns:
        str: spoken text
    """

    romanizedText = uroman.romanize_string(text)
    inputs = tokenizer(romanizedText, return_tensors="pt")

    with torch.no_grad():
        output = ttsModel(**inputs).waveform

    sampling_rate = ttsModel.config.sampling_rate
    sd.play(output.squeeze().numpy(), samplerate=sampling_rate)
    sd.wait()

    return text


messages = [{'role': 'user', 'content': prompt}]
print('Prompt:', messages[0]['content'])

available_functions = {
    'speak_korean': speak_korean,
}

response: ChatResponse = chat(
    llmModelName,
    messages=messages,
    tools=[speak_korean],
)

if response.message.tool_calls:
    # There may be multiple tool calls in the response
    for tool in response.message.tool_calls:
        # Ensure the function is available, and then call it
        if function_to_call := available_functions.get(tool.function.name):
            print('Calling function:', tool.function.name)
            print('Arguments:', tool.function.arguments)
            output = function_to_call(**tool.function.arguments)
            print('Function output:', output)
        else:
            print('Function', tool.function.name, 'not found')

# Only needed to chat with the model using the tool call results
if response.message.tool_calls:
    # Add the function response to messages for the model to use
    messages.append(response.message)
    messages.append({'role': 'tool', 'content': str(
        output), 'name': tool.function.name})

    # Get final response from model with function outputs
    final_response = chat('llama3.1', messages=messages)
    print('Final response:', final_response.message.content)

else:
    print('No tool calls returned from model')
