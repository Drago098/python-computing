import math

class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        final = 0
        for i in self.ledger:
            final += i["amount"]
        return final

    def transfer(self, amount, budget_cat):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {budget_cat.name}")
            budget_cat.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
        
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    #logic from Beau for most part, code original+snippet
    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for i in self.ledger:
            output += f"{i['description'][:23].ljust(23)}{format(i['amount'], '.2f').rjust(7)}\n" #code from Beau, for formatting
        output += f"Total: {format(self.get_balance(), '.2f')}"
        return output
        
def create_spend_chart(categories):
    category_names = []
    spent = []
    final_spent = []

    for category in categories: #logic from Beau, checking spent items
        total = 0
        for i in category.ledger:
            if i['amount'] < 0:
                total -= i['amount']
        spent.append(round(total, 2))
        category_names.append(category.name)

    for percents in spent:
        final_spent.append(round(percents/sum(spent), 2)*100)

    graph_return = "Percentage spent by category\n"

    axis = range(100,-10,-10)

    for label in axis: #logic from Beau, right alignment similar to arithmetic arranger
        graph_return += str(label).rjust(3) + "| "
        for percents in final_spent:
            if percents >= label:
                graph_return += "o  "
            else:
                graph_return += "   "
        graph_return += "\n"
                                                
    graph_return += "    ----" + ("---" * (len(category_names) - 1))
    graph_return += "\n     "

    len_longest = 0
    
    for names in category_names:
        if len_longest < len(names):
            len_longest = len(names)

    for i in range(len_longest): #logic from Beau, formatting
        for names in category_names:
            if len(names) > i:
                graph_return += names[i] + "  "
            else:
                graph_return += "   "
        if i < len_longest - 1:
            graph_return += "\n     "

    return graph_return
