using System.ComponentModel.DataAnnotations;

namespace BudgetTracker.Models.Entities
{
    public class Transaction:BaseEntity
    {
        public int TransactionId { get; set; }

        [Required]
        public decimal Amount { get; set; }
        [Required]
        public string Currency { get; set; } = "BGN";//Option for currency when user has paid in different currency
        [Required]
        public DateTime Date { get; set; }
        [MaxLength(100)]
        public string? Description { get; set; }
        [Required]
        public string Type { get; set; } = "Expense";//Expense or Income, etc.
        public int UserId { get; set; }
        public User User { get; set; }

    }
}
