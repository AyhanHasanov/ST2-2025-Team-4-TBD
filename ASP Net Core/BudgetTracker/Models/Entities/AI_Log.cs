using System.ComponentModel.DataAnnotations;

namespace BudgetTracker.Models.Entities
{
    public class AI_Log:BaseEntity
    {
        public int LogId { get; set; }

        public int UserId { get; set; }
        public User? User { get; set; }

        [Required]
        public string Query { get; set; }

        [Required]
        public string Response { get; set; } = string.Empty;

        public string Category { get; set; } // e.g. "BudgetAdvice", "Summary"
        public DateTime Timestamp { get; set; } = DateTime.UtcNow;
    }
}
