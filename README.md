# Banking-application
# Banking App System (Savings Account)

A simple demo banking app that models **Savings Account** behavior in two ways:

- **Web UI**: Deposit, Withdraw, and Apply **5% interest** in `index.html` (styled by `style.css`)
- **Python OOP**: `BankAccount` / `SavingsAccount` implementation in `banking-app.py`

---

## Files

- `index.html` — Browser-based UI (single page)
- `style.css` — Extra styling for the UI
- `javascript.js` — JavaScript class example (not currently connected to `index.html`)
- `banking-app.py` — Python OOP example + basic test run
- `README.md` — Project documentation

---

## Web App (Browser)

### How to run

1. Open `index.html` in your browser.
   - Double-click the file, or
   - Right-click → **Open with** → choose your browser.

### Features

- Starting balance displayed as **R1,000.00**
- **Deposit**: increases balance and updates **Total Deposited**
- **Withdraw**: validates the amount and ensures sufficient funds before subtracting
- **Apply 5% Interest**: calculates 5% of the current balance, adds it to the balance, and counts it as deposited

---

## Python App (OOP)

### Run command

1. Make sure Python is installed.
2. Run:

```bash
python banking-app.py
```

### Demonstrates

- **Encapsulation** via a “private” balance (`_balance`)
- Core methods:
  - `deposit(amount)`
  - `withdraw(amount)`
  - `calculate_interest()` in `SavingsAccount`
- **Inheritance**: `SavingsAccount` extends `BankAccount`

---

## Notes

- The web UI account logic is implemented directly inside `index.html` using an inline `<script>`.
- `javascript.js` mirrors the idea of the Python OOP model but is not wired into the UI.

---

## License

MIT (replace with your preferred license if needed).
