"""
Prompt templates for LLM requests.
These templates provide structured instructions to the Ollama model.
"""


def get_summarize_prompt(expenses: list) -> str:
    """
    Generate a prompt for expense summarization.
    
    Args:
        expenses: List of expense dictionaries with 'category' and 'amount' keys
        
    Returns:
        Formatted prompt string
    """
    expense_text = "\n".join([
        f"- {exp['category']}: ${exp['amount']:.2f}"
        for exp in expenses
    ])
    
    total = sum(exp['amount'] for exp in expenses)
    
    prompt = f"""You are a helpful financial assistant. Analyze the following expenses and provide a clear, natural-language summary.

Expenses:
{expense_text}

Total: ${total:.2f}

Please provide:
1. A brief overview of spending patterns
2. Which categories have the highest spending
3. Any notable observations about the expenses

Keep your response concise and actionable (3-4 sentences maximum)."""

    return prompt


def get_advice_prompt(question: str) -> str:
    """
    Generate a prompt for budgeting advice.
    
    Args:
        question: User's question about budgeting
        
    Returns:
        Formatted prompt string
    """
    prompt = f"""You are a helpful financial advisor specializing in personal budgeting. 

User Question: {question}

Provide a concise, practical budgeting tip or advice in response. Keep your answer clear and actionable (2-3 sentences maximum). Focus on practical steps the user can take."""

    return prompt


