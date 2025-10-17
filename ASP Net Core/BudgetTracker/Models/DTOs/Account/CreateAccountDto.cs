namespace BudgetTracker.Models.DTOs.Account
{
    public class CreateAccountDto
    {
        public string Name { get; set; }
        public string Currency { get; set; } = "BGN";
        public decimal Balance { get; set; } = 0;
        public string Description { get; set; }
    }
}
