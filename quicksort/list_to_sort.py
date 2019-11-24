class ListToSort:
  def __init__(self, list_to_sort):
    self.list = list_to_sort

  def Swap(self, index1, index2):
    element_a = self.list[index1]
    element_b = self.list[index2]
    self.list[index1] = element_b
    self.list[index2] = element_a

  def Larger(self, index1, index2):
    return self.list[index1] > self.list[index2]

  def Smaller(self, index1, index2):
    return self.list[index1] < self.list[index2]

  def Equal(self, index1, index2):
    return self.list[index1] == self.list[index2]

  def Length(self):
    return len(self.list)