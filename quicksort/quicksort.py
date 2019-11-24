from list_to_sort import ListToSort

# fuer die loesung alle '.list' weg
def Quicksort(listToSort: ListToSort) -> ListToSort:
  if listToSort.Length() == 0: return listToSort
  pivot_index = listToSort.Length()-1
  pivot_element = listToSort.list[pivot_index]
  i = 0
  j = pivot_index
  while i<j:
    while listToSort.list[i] < pivot_element: i += 1
    while listToSort.list[j] >= pivot_element and j > 0: j -= 1
    if i < j: listToSort.Swap(i, j)
  listToSort.Swap(pivot_index, i)
  sub_list_to_sort1 = ListToSort(listToSort.list[0:i])
  sub_list_to_sort2 = ListToSort(listToSort.list[i+1:])
  return ListToSort(Quicksort(sub_list_to_sort1).list + [pivot_element] + Quicksort(sub_list_to_sort2).list)

list_to_sort = ListToSort([1,2,3,6,1,2,3,3])

print(Quicksort(list_to_sort).list)