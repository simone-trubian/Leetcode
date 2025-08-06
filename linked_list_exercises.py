def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        previous_node = None
        while node.next:
            node.val = node.next.val
            previous_node = node
            node = node.next
        previous_node.next = None

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        i = 0
        nodes = []
        while node.next:
            node = node.next
            nodes.append(node)
            i += 1
        nodes.append(node)
        
        nodes[-(n+1)].val = nodes[-n].val
        nodes[-(n+1)].next = nodes[-n].next.next
        
        return head

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    node = head
    nodes = []
    while node.next:
        nodes.append(node)
        node = node.next
    nodes.append(node)
    
    # Linked list with one node only
    if len(nodes) == 1:
        head = None
    # Remove last node
    elif n == 1:
        nodes[-(n+1)].next = None
    # Remove head
    elif n == len(nodes):
        head = nodes[-(n-1)]
    else:
        nodes[-(n+1)].next = nodes[-(n-1)]
    
    return head                  

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None or head.next == None:
        return head
    
    node = head
    values = []
    while node.next:
        values.append(node.val)
        node = node.next
    values.append(node.val)
    
    values = list(reversed(values))
    node = head
    i = 0
    while node.next:
        node.val = values[i]
        node = node.next
        i += 1
    node.val = values[i]
    
    return head        

#def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1
    
    # Traverse first list and stich the two lists together
    current = list1
    while current.next:
        current = current.next
    current.next = list2
    
    # Traverse both lists to gather all values
    current = list1
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    # Sort values in merged list
    values = sorted(values)
    current = list1
    i = 0
    while current:
        current.val = values[i]
        current = current.next
        i += 1
    
    return list1

def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        node = head
        values = []
        while node.next:
            values.append(node.val)
            node = node.next
        values.append(node.val)
        
        for idx in range(len(values)//2):
            if values[idx] != values[(len(values)-(1+idx))]:
                return False
        
        return True

def alternativeIsPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        current=head
        while current:
            l.append(current.val)
            current=current.next
        return l==l[::-1]

def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = dict()
        index = 0
        current = head
        while current:
            if nodes.get(current):
                return True
            nodes[current] = index
            index += 1
            current = current.next
        return False
            

# Scan the list at two speeds, don't know how this works.
def alternativeHasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

# This algorithm destroys the values overwriting a None a value that
# can't be present in the original list. If the None seen again, the
# list has a cycle 
def alternative2hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == None:
                return True
            else:
                head.val = None
                head = head.next
        return False