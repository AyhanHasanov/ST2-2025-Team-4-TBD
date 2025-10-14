namespace BudgetTracker.Models.DTOs.Budget
{
    public class BudgetViewDto
    {
        public int BudgetId { get; set; }
        public decimal LimitAmount { get; set; }
        public string Currency { get; set; } = "BGN";
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }
        //public int CategoryId { get; set; }
        public string CategoryName { get; set; }
        public decimal SpentAmount { get; set; } = 0;
        public decimal RemainingAmount
        {
            get
            {
                var remaining = LimitAmount - SpentAmount;
                return remaining;
            }
        }
    }
}
