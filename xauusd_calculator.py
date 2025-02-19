from colorama import Fore, Style

def xauusd_calculator():
    print(Fore.CYAN + "\n★ XAUUSD Profit & Risk Calculator ★\n" + Style.RESET_ALL)
    
    # User Inputs
    balance = float(input(Fore.YELLOW + "Enter Account Size ($): " + Style.RESET_ALL))
    leverage_input = input(Fore.YELLOW + "Enter Leverage (e.g., 1:100, 1:500): " + Style.RESET_ALL)
    leverage = int(leverage_input.split(':')[1])
    lot_size = float(input(Fore.YELLOW + "Enter Lot Size (e.g., 0.1, 0.5, 1.0): " + Style.RESET_ALL))
    entry_price = float(input(Fore.YELLOW + "Enter Entry Price: " + Style.RESET_ALL))
    tp_price = float(input(Fore.YELLOW + "Enter Take Profit Price: " + Style.RESET_ALL))
    sl_price = float(input(Fore.YELLOW + "Enter Stop Loss Price: " + Style.RESET_ALL))
    position_type = input(Fore.YELLOW + "Enter Position Type (BUY/SELL): " + Style.RESET_ALL).upper()
    
    # Pip Calculation (XAUUSD moves in 0.1 pips)
    if position_type == "BUY":
        profit_pips = (tp_price - entry_price) / 0.1
        sl_pips = (entry_price - sl_price) / 0.1
    else:  # SELL Position
        profit_pips = (entry_price - tp_price) / 0.1
        sl_pips = (sl_price - entry_price) / 0.1
    
    # Profit Calculation (1 Pip = $10 per 1.0 Lot, so 0.1 Lot = $1 per Pip)
    profit_per_pip = lot_size * 10
    total_profit = profit_pips * profit_per_pip
    total_loss = sl_pips * profit_per_pip
    
    # Margin Calculation
    required_margin = (entry_price * lot_size * 100) / leverage
    
    # Display Results
    print(Fore.GREEN + f"\n★ Total Profit Pips: {profit_pips:.2f} Pips")
    print(Fore.RED + f"★ Total SL Pips: {sl_pips:.2f} Pips")
    print(Fore.GREEN + f"★ Total Profit (if TP hits): ${total_profit:.2f}")
    print(Fore.RED + f"★ Total Loss (if SL hits): ${total_loss:.2f}")
    print(Fore.MAGENTA + f"★ Required Margin: ${required_margin:.2f} (Available: ${balance})\n" + Style.RESET_ALL)
    
    # Risk Warning
    if total_loss > balance:
        print(Fore.RED + "⚠ Warning: Your SL Risk is higher than your account balance! Margin Call Possible!" + Style.RESET_ALL)
    elif required_margin > balance:
        print(Fore.RED + "⚠ Warning: Insufficient Balance to Open This Position!" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "✔ You can safely open this position." + Style.RESET_ALL)

# Run the calculator
xauusd_calculator()