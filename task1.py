class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    linked_list.head = prev

def merge_sort_list(linked_list):
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    def get_middle(node):
        if not node:
            return node
        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_lists(left_head, right_head):
        dummy_node = ListNode(0)
        tail = dummy_node
        while left_head and right_head:
            if left_head.value <= right_head.value:
                tail.next = left_head
                left_head = left_head.next
            else:
                tail.next = right_head
                right_head = right_head.next
            tail = tail.next
        if left_head:
            tail.next = left_head
        elif right_head:
            tail.next = right_head
        return dummy_node.next

    middle = get_middle(linked_list.head)
    next_to_middle = middle.next
    middle.next = None

    left = LinkedList()
    left.head = linked_list.head
    right = LinkedList()
    right.head = next_to_middle

    left = merge_sort_list(left)
    right = merge_sort_list(right)

    sorted_list = merge_lists(left.head, right.head)
    linked_list.head = sorted_list
    return linked_list

def merge_sorted_lists(list1, list2):
    dummy_head = ListNode(0)
    tail = dummy_head
    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    return dummy_head.next

# Створюю та заповнюю пов’язані списки для тестування
list1 = LinkedList()
list2 = LinkedList()
for value in [7, 2, 4, 3, 5]:
    list1.append(value)
for value in [1, 6, 8, 9, 10]:
    list2.append(value)

# Оригінальні списки
original_list1 = list1.to_list()
original_list2 = list2.to_list()

# Реверсивний список
reverse_list(list1)
reversed_list1 = list1.to_list()

# Сортування для однозв'язного списку
sorted_list2 = merge_sort_list(list2).to_list()

# Об'єднання двох відсортованих однозв'язних списків
merged_sorted_list = merge_sorted_lists(ListNode(3), ListNode(1))
merged_sorted_list_values = [merged_sorted_list.value, merged_sorted_list.next.value]

print(f"Оригінальний однозвʼязний список 1: {original_list1}")
print(f"Результат функції реверсування однозв'язного списку: {reversed_list1}")
print(f"Оригінальний однозвʼязний список 1: {original_list2}")
print(f"Алгоритм сортування для однозв'язного списку: {sorted_list2}")
print(f"Об'єднання двох відсортованих однозв'язних списків в один: {merged_sorted_list_values}")
