import heapq

def merge_k_lists(lists):
   min_heap = []
   merged_list = []

   # Ініціалізуємо купу першими елементами кожного списку
   for i, l in enumerate(lists):
      if l:
          heapq.heappush(min_heap, (l[0], i, 0))

   while min_heap:
      val, list_index, element_index = heapq.heappop(min_heap)
      merged_list.append(val)

      # Якщо є наступний елемент в списку, додаємо його до купи
      if element_index + 1 < len(lists[list_index]):
         heapq.heappush(min_heap, (lists[list_index][element_index + 1], list_index, element_index + 1)) 
   return  merged_list     


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list) 