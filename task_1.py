import heapq

def min_cost_to_connect_cables(cables_lengths):
   #  ініціалізуємо купу
   heapq.heapify(cables_lengths)
   
   #  визначаємо загальну вартість
   total_cost = 0

   #  поки купа не пуста
   while len(cables_lengths) > 1:
      #  вибираємо два найменших елементи
      a = heapq.heappop(cables_lengths)
      b = heapq.heappop(cables_lengths)
      
      #  додаємо вартість з'єднання
      total_cost += a + b
      
      #  додаємо новий кабель до купи
      heapq.heappush(cables_lengths, a + b)

   return total_cost

cable_lengths = [4, 3, 2, 6]
print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))
