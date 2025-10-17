using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;

namespace BudgetTracker.Models.Entities
{
    public class ApplicationUser:IdentityUser
    {
        // From BaseEntity
        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
        public DateTime ModifiedAt { get; set; }

        // From User model
        [PersonalData]
        [Required, MaxLength(50)]
        public string? FirstName { get; set; }
        [PersonalData]
        [Required, MaxLength(50)]
        public string? LastName { get; set; }

        public string PreferredCurrency { get; set; } = "BGN";
        public string Language { get; set; } = "bg";

        // Navigation properties
        public ICollection<Transaction> Transactions { get; set; } = new List<Transaction>();
        public ICollection<Category> Categories { get; set; } = new List<Category>();
        public ICollection<Budget> Budgets { get; set; } = new List<Budget>();
        public ICollection<AI_Log> AI_Logs { get; set; } = new List<AI_Log>();


    }
}
