from ollama import ChatResponse, chat
from transformers import VitsModel, AutoTokenizer
import torch
import uroman as ur
import sounddevice as sd

prompt = 'You are an English speaking teacher for the Korean language. Speak a short Korean sentence with the given tool. And then ask me what it means.'
llmModelName = 'qwen2.5'

print("Loading TTS models")
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


available_functions = {
    'speak_korean': speak_korean,
}

messages = [{'role': 'user', 'content': prompt}]
print('Prompt:', messages[0]['content'])
response: ChatResponse = chat(
    llmModelName,
    messages=messages,
    tools=[speak_korean],
)

if response.message.tool_calls:
    assistant_message_with_tools = response.message
    # Add assistant's request for tool calls
    messages.append(assistant_message_with_tools)

    for tool_call in assistant_message_with_tools.tool_calls:
        function_name = tool_call.function.name
        function_args = tool_call.function.arguments

        if function_to_call := available_functions.get(function_name):
            print(f'Calling function: {function_name}')
            print(f'Arguments: {function_args}')
            try:
                tool_output_content = function_to_call(**function_args)
                print(f'Function output: {tool_output_content}')
                messages.append({
                    'role': 'tool',
                    'content': str(tool_output_content),
                    'name': function_name,
                })
            except Exception as e:
                print(f"Error calling function {function_name}: {e}")
                messages.append({
                    'role': 'tool',
                    'content': f"Error executing tool {function_name}: {str(e)}",
                    'name': function_name,
                })
        else:
            print(f'Function {function_name} not found')
            messages.append({
                'role': 'tool',
                'content': f"Function {function_name} not found.",
                'name': function_name,
            })
else:
    print('No tool calls were made by the model.')
    if response.message.content:
        print("LLM's direct response:", response.message.content)


# Get user's answer and decide if it was correct
user_answer = input("Your answer: ")
teacher_check_answer_prompt = f"The user thinks the answer is '${user_answer}' Is this answer correct?"
messages.append({'role': 'user', 'content': teacher_check_answer_prompt})

# Get LLM's evaluation of the answer
print("\nTeacher is evaluating your answer...")
evaluation_response = chat(llmModelName, messages=messages)
print('Teacher:', evaluation_response.message.content)
