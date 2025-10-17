namespace BudgetTracker.Models.DTOs.Transaction
{
    public class UpdateTransactionDto
    {
        public int TransactionId { get; set; }
        public decimal Amount { get; set; }
        public string Currency { get; set; } = "BGN";
        public DateTime Date { get; set; }
        public string? Description { get; set; }
        public string Type { get; set; } = "Expense";
    }
}
