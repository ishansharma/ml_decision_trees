class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Lets you know if Stack is empty
        Returns
        -------
        bool
        """
        return self.items == []

    def push(self, item):
        """
        Add item to the stack
        Parameters
        ----------
        item
            Can be anything. For this project, it will be a tuple

        Returns
        -------
        None
        """
        self.items.append(item)

    def pop(self):
        """
        Pop top element and return
        """
        return self.items.pop()

    def size(self):
        """
        Return the size of stack
        Returns
        -------
        int
        """
        return len(self.items)
