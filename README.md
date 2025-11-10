# Test Repository for RAGAS Evaluation

This is an example test repository structure for RAGAS evaluation testing.

## Structure

```
test_repo_example/
├── evals/
│   └── data.json          # Evaluation dataset
├── ai/
│   └── pipeline.py        # Pipeline with entrypoint function
└── README.md             # This file
```

## Files

### `evals/data.json`
Contains the evaluation dataset with questions, contexts, and ground truth answers.

Each item has:
- `query`: The question to answer
- `context`: Context information (string or list)
- `answer`: Ground truth answer

### `ai/pipeline.py`
Contains the entrypoint function `answer_question` that:
1. Takes query, context, and model_config
2. Calls OpenAI API
3. Returns generated answer

## Usage

### Step 1: Create GitHub Repository

1. Create a new GitHub repository
2. Copy these files to your repository
3. Push to GitHub:

```bash
git init
git add .
git commit -m "Add RAGAS evaluation files"
git remote add origin https://github.com/yourusername/your-test-repo.git
git branch -M main
git push -u origin main
```

### Step 2: Update API Key

When calling the evaluation API, provide your OpenAI API key:

```bash
curl -X POST http://localhost:8000/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/yourusername/your-test-repo.git",
    "commit_sha": "main",
    "entrypoint": "ai/pipeline.py:answer_question",
    "dataset": "evals/data.json",
    "model_provider": "openai",
    "model_name": "gpt-4o-mini",
    "openai_api_key": "sk-your-actual-api-key-here"
  }'
```

### Step 3: Check Results

```bash
curl http://localhost:8000/result/{job_id}
```

## Expected Results

You should get metrics like:

```json
{
  "faithfulness": 0.85-0.95,
  "answer_relevancy": 0.80-0.90,
  "total_items": 5
}
```

## Customization

### Add More Data

Edit `evals/data.json` to add more test cases:

```json
{
  "query": "Your question?",
  "context": "Your context information",
  "answer": "Ground truth answer"
}
```

### Modify Pipeline

Edit `ai/pipeline.py` to change:
- Prompt template
- Model parameters (temperature, max_tokens)
- System message
- Response formatting

### Use Different Models

In the API request, change:
- `"model_name": "gpt-4"` for GPT-4
- `"model_name": "gpt-3.5-turbo"` for GPT-3.5

## Testing Locally

You can test the pipeline function locally:

```python
from ai.pipeline import answer_question

model_config = {
    "api_key": "sk-your-key",
    "name": "gpt-4o-mini",
    "temperature": 0.3
}

answer = answer_question(
    query="What is diabetes?",
    context_docs="Diabetes is a disease of high blood sugar.",
    model_config=model_config
)

print(answer)
```

## Troubleshooting

### Issue: API Key Error
Make sure your OpenAI API key is valid and has credits.

### Issue: Low Scores
Try:
- Improving the prompt
- Lowering temperature
- Using a better model (gpt-4)
- Ensuring context contains relevant info

### Issue: Function Not Found
Verify entrypoint path: `"ai/pipeline.py:answer_question"`

