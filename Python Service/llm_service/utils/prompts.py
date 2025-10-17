def get_summarize_prompt(expenses: list, budget: float) -> str:
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
    
    prompt = f"""You are a helpful financial assistant. Analyze the following expenses and provide a clear, natural-language summary in 1-2 sentence(s).
Budget: {budget:.2f}

Expenses:
{expense_text}

Total: ${total:.2f}

Please provide:
1. Which categories have the highest spending
2. Any notable observations about the expenses

Keep your response concise and actionable (2 sentences maximum). Exclude any markdown formatting and formatting at all!"""

    return prompt


def get_advice_prompt(question: str, expenses: list, budget: float) -> str:
    """
    Generate a prompt for budgeting advice.
    
    Args:
        question: User's question about budgeting
        expenses: List of expense dictionaries with 'category' and 'amount' keys
        budget: User's budget amount
        
    Returns:
        Formatted prompt string
    """
    expense_text = "\n".join([
        f"- {exp['category']}: ${exp['amount']:.2f}"
        for exp in expenses
    ])
    
    total = sum(exp['amount'] for exp in expenses)
    remaining = budget - total
    budget_status = "over budget" if remaining < 0 else "under budget" if remaining > 0 else "exactly at budget"
    
    prompt = f"""You are a helpful financial advisor specializing in personal budgeting. 

User Question: {question}
Budget: ${budget:.2f}
Current Expenses:
{expense_text}

Total Spending: ${total:.2f}
Remaining Budget: ${remaining:.2f} ({budget_status})

Analyze the relationship between the expenses and the budget. Based on the user's specific expenses and their budget of ${budget:.2f}, provide a concise, practical budgeting tip or advice in response. Keep your answer clear and actionable (2-3 sentences maximum). Focus on practical steps the user can take to improve their financial situation and stay within budget."""

    return prompt


