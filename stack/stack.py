

class Stack:
    def __init__(self):
        self.st = []

    def length_of_stack(self):
        return len(self.st)

    def push_item_to_stack(self,value):
        self.st.insert(0,value)

    def peek_element(self):
        if self.length_of_stack() == 0:
            raise Exception("Hey You're stack is empty")
        else:
            return self.st[0]

    def pop_element(self):
        if self.length_of_stack() == 0:
            raise Exception("Hey you're stack is empty")
        else:
            return self.st.pop(0)


stack_construct = Stack()
stack_construct.push_item_to_stack(10)
stack_construct.push_item_to_stack(20)
stack_construct.push_item_to_stack(30)
stack_construct.push_item_to_stack(40)
print(stack_construct.peek_element())
# stack_construct.pop_element()