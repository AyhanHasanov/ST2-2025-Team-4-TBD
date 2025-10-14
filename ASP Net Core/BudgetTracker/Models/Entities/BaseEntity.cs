namespace BudgetTracker.Models.Entities
{
    abstract public class BaseEntity
    {
        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
        public DateTime ModifiedAt { get; set; }




    }
}
