from transformers import pipeline

# Load small open-source model
generator = pipeline(
    "text-generation",
    model="distilgpt2",
)

def generate_doc(code_chunk):
    prompt = f"""
    Generate professional Python documentation for this function:

    {code_chunk}

    Documentation:
    """

    result = generator(
        prompt,
        max_length=300,
        num_return_sequences=1,
    )

    return result[0]["generated_text"]
