namespace BudgetTracker.Models.Entities
    
{
    public class Budget:BaseEntity
    {
        public int BudgetId { get; set; }
        public decimal LimitAmount { get; set; }
        public decimal CurrentSpent { get; set; } 
        public string Currency { get; set; } = "BGN";
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }
        public int UserId { get; set; }
        public User User { get; set; }
        public int CategoryId { get; set; }
        public Category Category { get; set; }
    }
}
