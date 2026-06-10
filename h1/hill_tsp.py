import math
import random
import matplotlib.pyplot as plt

# 1. 定義城市座標 (100*100 範圍內的 8 個點)
cities = {
    'A': (10, 10), 'B': (25, 80), 'C': (45, 15), 'D': (55, 90),
    'E': (80, 10), 'F': (95, 85), 'G': (50, 50), 'H': (15, 45)
}

def calculate_distance(route):
    """計算整條路徑的總長度（包含回到起點）"""
    total = 0
    for i in range(len(route)):
        c1 = cities[route[i]]
        c2 = cities[route[(i + 1) % len(route)]] # 回到起點
        total += math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
    return total

def hill_climbing(max_iterations=1000):
    # 隨機產生一個初始解
    current_route = list(cities.keys())
    random.shuffle(current_route)
    current_dist = calculate_distance(current_route)
    
    print(f"初始路徑: {current_route}")
    print(f"初始距離: {current_dist:.2f}\n")

    for i in range(max_iterations):
        # 產生鄰居：隨機交換兩個城市的位置
        neighbor_route = current_route[:]
        idx1, idx2 = random.sample(range(len(neighbor_route)), 2)
        neighbor_route[idx1], neighbor_route[idx2] = neighbor_route[idx2], neighbor_route[idx1]
        
        neighbor_dist = calculate_distance(neighbor_route)
        
        # 如果鄰居比較好，就移動過去
        if neighbor_dist < current_dist:
            current_route = neighbor_route
            current_dist = neighbor_dist
            print(f"第 {i+1} 次迭代: 找到更好的路徑 {current_route}, 距離: {current_dist:.2f}")
            
    return current_route, current_dist

# 執行演算法
best_path, min_dist = hill_climbing()
print(f"\n最終優化路徑: {best_path}")
print(f"最終最短距離: {min_dist:.2f}")

# 繪製路徑圖
x = [cities[city][0] for city in best_path + [best_path[0]]]
y = [cities[city][1] for city in best_path + [best_path[0]]]
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o-', markersize=8, linewidth=2)
for i, city in enumerate(best_path):
    plt.text(cities[city][0], cities[city][1], city, fontsize=12, ha='right')
plt.title('TSP Hill Climbing Best Path')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()