using System.ComponentModel.DataAnnotations;

namespace BudgetTracker.Models.Entities
{
    public class Transaction : BaseEntity
    {
        [Required]
        public decimal Amount { get; set; }

        [Required, StringLength(3)]
        public string Currency { get; set; } = "BGN"; // Use ISO codes

        [Required]
        public DateTime Date { get; set; }

        [MaxLength(100)]
        public string? Description { get; set; }

        [Required]
        public string Type { get; set; } = "Expense";

        // Relationships
        [Required]
        public string UserId { get; set; } = string.Empty;
        public ApplicationUser User { get; set; }

        // Optional link to Budget (if applicable)
        public int? BudgetId { get; set; }
        public Budget? Budget { get; set; }

        // Optional link to Category
        public int? CategoryId { get; set; }
        public Category? Category { get; set; }
    }
}
