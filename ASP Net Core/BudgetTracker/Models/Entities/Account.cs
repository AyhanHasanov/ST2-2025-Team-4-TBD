using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace BudgetTracker.Models.Entities
{
    public class Account : BaseEntity
    {
        [Required]
        public string Name { get; set; } // e.g., "Main Checking", "Wallet", "PayPal"

        [Required]
        public string Currency { get; set; } = "BGN"; // default currency

        [Required]
        public decimal Balance { get; set; } = 0; // current balance in account

        public string Description { get; set; } // optional notes

        [Required]
        public string UserId { get; set; } // link to ApplicationUser
        public ApplicationUser User { get; set; }

        // Navigation: transactions related to this account
        public ICollection<Transaction> Transactions { get; set; }
    }
}
