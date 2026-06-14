//JS class recreating Python OOP logic

class SavingAccount {
    constructor(accountHolder, initialBalance = 0.0, interestRate = 0.05) {
        this.accountHolder = accountHolder;
        // Symbolizes the private_balance in Python
        this.balance = Math.max(0.0, initialBalance);
        this.interestRate = interestRate;
    }

    getBalance() {
        return this.balance;
    }

    deposit(amount) {
        if (amount > 0) {
            this.balance += amount;
        }
    }
}

//add Loading spinner to the page
function showLoadingSpinner() {
    const spinner = document.createElement('div');
    spinner.className = 'loading-spinner';
    document.body.appendChild(spinner);
}
