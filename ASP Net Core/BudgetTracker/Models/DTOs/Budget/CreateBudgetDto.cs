using BudgetTracker.Models.Entities;

namespace BudgetTracker.Models.DTOs.Budget
{
    public class CreateBudgetDto
    {
        public int BudgetId { get; set; }
        public decimal LimitAmount { get; set; }
        public string Currency { get; set; } = "BGN";
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }
        public int CategoryId { get; set; }
    }
}
