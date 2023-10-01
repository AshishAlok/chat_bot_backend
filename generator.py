from transformers import AutoTokenizer, pipeline
import torch

# Load the tokenizer and text-generation pipeline
model = "meta-llama/Llama-2-7b-chat-hf"

# HF_TOKEN = "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"


tokenizer = AutoTokenizer.from_pretrained(model)

generator = pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float32,
    device_map="auto",
)

# Function to generate responses
def generate_response( question):
    INBUILT_PROMPT = "Identify yourself as a character in the Bhagavad Gita, preferably Krishna or Dronacharya, and answer the question asked. You should also state a quote that describes the question or its solution."
    
    # Construct the prompt with the provided character, quote, question, and answer
    prompt = f"{INBUILT_PROMPT}\nQuestion: {question}\n"
    
    response = pipeline(
        prompt,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=200,
    )[0]

    generated_text_lines = response['generated_text'].split('\n')
    modified_text = '\n'.join(generated_text_lines[2:])
    
    return modified_text




# print(generate_response("hi i am dperessed"))