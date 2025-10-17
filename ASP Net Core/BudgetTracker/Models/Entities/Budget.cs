using System.ComponentModel.DataAnnotations;

namespace BudgetTracker.Models.Entities
    
{
    public class Budget:BaseEntity
    {
        [Required]
        public decimal BudgetAmount { get; set; }  // Max budget for this period

        [Required]
        public DateTime StartDate { get; set; }   // Period start

        [Required]
        public DateTime EndDate { get; set; }     // Period end

        [Required]
        public string UserId { get; set; }
        public ApplicationUser? User { get; set; }
        public ICollection<Transaction>? Transactions { get; set; }
    }
}
