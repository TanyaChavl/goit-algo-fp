def greedy_algorithm(items, budget):
    # Підготовка списку страв зі співвідношенням калорій до вартості
    cost_per_calorie = [(name, item["calories"] / item["cost"]) for name, item in items.items()]
    # Сортування списку за співвідношенням калорій до вартості у спадному порядку
    cost_per_calorie.sort(key=lambda x: x[1], reverse=True)
    
    total_calories = 0
    selected_items = []
    for name, _ in cost_per_calorie:
        item_cost = items[name]["cost"]
        if budget - item_cost >= 0:
            budget -= item_cost
            total_calories += items[name]["calories"]
            selected_items.append(name)
        if budget <= 0:
            break

    return selected_items, total_calories

def dynamic_programming(items, budget):
    item_list = list(items.keys())
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    
    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            if items[item_list[i-1]]["cost"] <= w:
                dp[i][w] = max(items[item_list[i-1]]["calories"] + dp[i-1][w-items[item_list[i-1]]["cost"]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Відновлення списку вибраних страв
    w = budget
    n = len(items)
    selected_items = []
    while n > 0:
        if dp[n][w] != dp[n-1][w]:
            selected_items.append(item_list[n-1])
            w -= items[item_list[n-1]]["cost"]
        n -= 1
    
    total_calories = dp[len(items)][budget]
    return selected_items[::-1], total_calories

# Вхідні дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

# Перевірка роботи функцій
greedy_result = greedy_algorithm(items, budget)
dynamic_result = dynamic_programming(items, budget)

print(f"Принцип жадібного алгоритму: {greedy_result}")
print(f"Принцип динамічного програмування: {dynamic_result}")
