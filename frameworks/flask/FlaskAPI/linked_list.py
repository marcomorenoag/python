class Node:
  def __init__(self, data = None, next_node = None):
    self.data = data
    self.next_node = next_node

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  def to_list(self):
    listItems = []
    if self.head is None:
      return listItems
    node = self.head
    while node:
      listItems.append(node.data)
      node = node.next_node
    return listItems
  def get_user_by_id(self, user_id):
    node = self.head
    while node:
      if node.data['id'] is int(user_id):
        return node.data
      node = node.next_node
    return None
  def insert_beginning(self, data):
    if self.head is None:
      self.head = Node(data, None)
      self.tail = self.head
    else:
      new_node = Node(data, self.head)
      self.head = new_node
  def insert_at_end(self, data):
    if self.head is None:
      self.insert_beginning(data)
    self.tail.next_node = Node(data, None)
    self.tail = self.tail.next_node
  def print_ll(self):
    ll_string = ''
    node = self.head
    if node is None:
      print(None)
    while node:
      ll_string += f' {str(node.data)} ->'
      node = node.next_node
    ll_string += ' None'
    print(ll_string)


if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_beginning('data1')
  ll.insert_beginning('data2')
  ll.insert_beginning('data3')
  ll.insert_beginning('data4')
  ll.insert_beginning('data5')
  ll.insert_beginning('data6')
  ll.insert_beginning('data7')
  ll.insert_beginning('data8')
  ll.insert_at_end('data9')
  ll.insert_at_end('data10')
  ll.print_ll()
