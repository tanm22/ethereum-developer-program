import random
import matplotlib.pyplot as plt

def simulate_strategy(strategy, num_bets, N=None, M=None):
    T = 2
    total_profit = 0
    net_profit = []
    consecutive_losses = 0
    consecutive_wins = 0
    
    for bet in range(num_bets):
        roll = random.uniform(0, 100)
        win_multiplier = 1 + (T / (100 - T)) - 0.01
        
        if strategy == 'fixed':
            win = roll > T
        elif strategy == 'alternating':
            if (bet // N) % 2 == 0:
                win = roll > T
            else:
                win = roll <= T
        elif strategy == 'progressive':
            win = roll > T
            T = max(2, min(100, T + 1 if win else T - 1))
        elif strategy == 'resetting':
            win = roll > T
            if win:
                consecutive_wins += 1
                consecutive_losses = 0
                if consecutive_wins >= M:
                    T = 2
                    consecutive_wins = 0
            else:
                consecutive_losses += 1
                consecutive_wins = 0
                if consecutive_losses >= N:
                    T = 2
                    consecutive_losses = 0
        
        if win:
            total_profit += win_multiplier - 1
        else:
            total_profit -= 1
        
        net_profit.append(total_profit)
    
    return net_profit

# Parameters
num_bets = 10000

# Simulate each strategy
fixed_profit = simulate_strategy('fixed', num_bets)
alternating_profit = simulate_strategy('alternating', num_bets, N=100)
progressive_profit = simulate_strategy('progressive', num_bets)
resetting_profit = simulate_strategy('resetting', num_bets, N=3, M=3)

# Plot results
plt.figure(figsize=(14, 8))
plt.plot(fixed_profit, label="Fixed Strategy")
plt.plot(alternating_profit, label="Alternating Strategy")
plt.plot(progressive_profit, label="Progressive Strategy")
plt.plot(resetting_profit, label="Resetting Strategy")
plt.xlabel('Number of Bets')
plt.ylabel('Net Profit')
plt.title('Net Profit vs Number of Bets')
plt.legend()
plt.grid(True)
plt.show()
