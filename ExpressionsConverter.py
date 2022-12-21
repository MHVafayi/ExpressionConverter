class Converter:
    def __init__(self):
        self.stack = []
        self.priorities = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, "(": 4, ')': 4}

    def prefix_to_infix(self, expression: str):
        for char in expression[::-1]:
            if char == " ":
                continue
            elif char.isalnum():
                self.stack.append(char)
            else:
                operand1 = self.stack.pop()
                operand2 = self.stack.pop()
                self.stack.append('(' + operand1 + char + operand2 + ')')
        return self.stack.pop()[1:-1]

    def postfix_to_infix(self, expression: str):
        for char in expression:
            if char == " ":
                continue
            elif char.isalnum():
                self.stack.append(char)
            else:
                operand1 = self.stack.pop()
                operand2 = self.stack.pop()
                self.stack.append('(' + operand2 + char + operand1 + ')')
        return self.stack.pop()[1:-1]

    def postfix_to_prefix(self, expression: str):
        for char in expression:
            if char == " ":
                continue
            elif char.isalnum():
                self.stack.append(char)
            else:
                operand1 = self.stack.pop()
                operand2 = self.stack.pop()
                self.stack.append(char + operand2 + operand1)
        return self.stack.pop()

    def prefix_to_postfix(self, expression: str):
        for char in expression[::-1]:
            if char == " ":
                continue
            elif char.isalnum():
                self.stack.append(char)
            else:
                # char is operator
                operand1 = self.stack.pop()
                operand2 = self.stack.pop()
                self.stack.append(operand1 + operand2 + char)
        return self.stack.pop()

    def infix_to_prefix(self, expression: str):
        operators = []
        for char in expression:
            if char == " ":
                continue
            elif char.isalnum():
                self.stack.append(char)
            elif char == "(":
                operators.append("(")
            elif char == ")":
                try:
                    while operators[-1] != "(":
                        operand1 = self.stack.pop()
                        operand2 = self.stack.pop()
                        operator = operators.pop()
                        self.stack.append(operator + operand2 + operand1)
                    operators.pop()
                except IndexError:
                    raise Exception("you have used single parenthesis instead of two!")
            else:
                while len(operators) > 0 and operators[-1] != '(' and self.is_second_operator_greater_or_equal(char, operators[-1]):
                    operand1 = self.stack.pop()
                    operand2 = self.stack.pop()
                    operator = operators.pop()
                    self.stack.append(operator + operand2 + operand1)
                operators.append(char)
        while len(operators) != 0:
            operand1 = self.stack.pop()
            operand2 = self.stack.pop()
            operator = operators.pop()
            self.stack.append(operator + operand2 + operand1)
        return self.stack.pop()

    def is_second_operator_greater_or_equal(self, operator1: str, operator2: str):
        priority1 = self.priorities.get(operator1)
        if not isinstance(priority1, int):
            priority1 = 0
        priority2 = self.priorities.get(operator2)
        if not isinstance(priority2, int):
            priority2 = 0
        return priority1 <= priority2

    def edit_priorities(self, operator: str, priority: int):
        if len(operator) != 1:
            raise Exception("you should enter a single character!")
        if operator.isalnum():
            raise Exception("you should enter non-alphabetic character!")
        if operator == "(" or operator == ")":
            raise Exception("this character has the highest priority and you can't change it!")
        self.priorities[operator] = priority
        if priority >= self.priorities.get(')'):
            self.priorities[')'] = priority + 1
            self.priorities['('] = priority + 1

    def infix_to_postfix(self, expression: str):
        operators = []
        for char in expression:
            if char == " ":
                continue
            elif char.isalnum():
                self.stack.append(char)
            elif char == '(':
                operators.append('(')
            elif char == ')':
                try:
                    while operators[-1] != '(':
                        operator = operators.pop()
                        operand1 = self.stack.pop()
                        operand2 = self.stack.pop()
                        self.stack.append(operand2 + operand1 + operator)
                    operators.pop()
                except IndexError:
                     raise Exception("you have used single parenthesis instead of two!")
            else:
                while len(operators) > 0 and operators[-1] != '(' and self.is_second_operator_greater_or_equal(char, operators[-1]):
                    operator = operators.pop()
                    operand1 = self.stack.pop()
                    operand2 = self.stack.pop()
                    self.stack.append(operand2+operand1+operator)
                operators.append(char)
        while len(operators) > 0:
            operator = operators.pop()
            operand1 = self.stack.pop()
            operand2 = self.stack.pop()
            self.stack.append(operand2+operand1+operator)
        return self.stack.pop()

