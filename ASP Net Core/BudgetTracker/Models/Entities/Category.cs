namespace BudgetTracker.Models.Entities
{
    public class Category:BaseEntity
    {
        public int CategoryId { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public int UserId { get; set; }
        public User User { get; set; }
    }
}
