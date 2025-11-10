"""Example pipeline for RAGAS evaluation testing."""

from openai import OpenAI


def answer_question(query, context_docs, model_config):
    """
    Generate an answer using OpenAI's API.
    
    This is the entrypoint function that RAGAS will call for each
    item in the evaluation dataset.
    
    Args:
        query: The question to answer (string)
        context_docs: Context information - can be:
                     - A single string
                     - A list of strings
        model_config: Configuration dict containing:
                     - 'api_key': OpenAI API key
                     - 'name': Model name (e.g., 'gpt-4o-mini')
                     - Optional: 'temperature', 'max_tokens', etc.
    
    Returns:
        Generated answer as a string
    """
    # Initialize OpenAI client with API key from config
    client = OpenAI(api_key=model_config.get("api_key"))
    
    # Handle context as string or list
    if isinstance(context_docs, list):
        context = "\n".join(context_docs)
    else:
        context = str(context_docs)


    
    
    # Create prompt that emphasizes using only the context
    prompt = f"""Context:
{context}

Question: {query}

Provide a concise answer based ONLY on the information in the context above. 
If the context doesn't contain enough information, say so."""
    
    # Get configuration parameters
    model_name = model_config.get("name", "gpt-4o-mini")
    temperature = model_config.get("temperature", 0.3)
    max_tokens = model_config.get("max_tokens", 150)
    
    # Call OpenAI API
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that answers questions based on the provided context."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    # Return the generated answer
    return response.choices[0].message.content


# Alternative: Simple mock implementation for testing without API key
def answer_question_mock(query, context_docs, model_config):
    """
    Mock implementation that doesn't require API calls.
    Useful for testing the pipeline without incurring API costs.
    """
    # Handle context as string or list
    if isinstance(context_docs, list):
        context = "\n".join(context_docs)
    else:
        context = str(context_docs)
    
    # Simple mock response
    return f"Based on the context about '{query}', here is a summary: {context[:100]}..."

