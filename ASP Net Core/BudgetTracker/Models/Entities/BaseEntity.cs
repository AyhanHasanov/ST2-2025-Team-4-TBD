using System.ComponentModel.DataAnnotations;

namespace BudgetTracker.Models.Entities
{
    abstract public class BaseEntity
    {
        [Key]
        public int Id { get; set; }
        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
        public string? CreatedBy { get; set; }
        public DateTime ModifiedAt { get; set; }
        public string? ModifiedBy { get; set; }




    }
}
