namespace BudgetTracker.Models.DTOs.Budget
{
    public class BudgetViewDto
    {
        public int BudgetId { get; set; }
        public decimal BudgetAmount { get; set; }
        public string Currency { get; set; } = "BGN";
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }

        //logic will be incorporated in service/controller
        public decimal SpentAmount { get; set; }
        public decimal IncomeAmount { get; set; }
        public decimal RemainingAmount { get; set; }
        public bool InLimit { get; set; }
        public bool Exceeded { get; set; }
    }
}
