using System.ComponentModel.DataAnnotations;

namespace BudgetTracker.Models.Entities
{
    public class User:BaseEntity
    {
        public int UserId { get; set; }
        [Required, EmailAddress]
        public string Email { get; set; }
        [Required]
        public string PasswordHash { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string PhoneNumber { get; set; }
        public string PreferredCurrency { get; set; } = "BGN";
        public string Language { get; set; } = "bg";
        public ICollection<Transaction>? Transactions { get; set; }
        public ICollection<Category>? Categories { get; set; }
        public ICollection<Budget>? Budgets { get; set; }
        public ICollection<AI_Log>? AI_Logs { get; set; }

    }
}
