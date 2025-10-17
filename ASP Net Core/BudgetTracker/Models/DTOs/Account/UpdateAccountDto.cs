namespace BudgetTracker.Models.DTOs.Account
{
    public class UpdateAccountDto
    {
        public string Name { get; set; }
        public string Currency { get; set; }
        public decimal Balance { get; set; }
        public string Description { get; set; }
    }
}
