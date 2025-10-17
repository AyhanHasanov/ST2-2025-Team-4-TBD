using BudgetTracker.Models.Entities;

namespace BudgetTracker.Models.DTOs.Budget
{
    public class CreateBudgetDto
    {
        public decimal BudgetAmount { get; set; }
        public string Currency { get; set; } = "BGN";
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }
    }
}
