class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        if amount <= total:
            return True
        return False

    def __str__(self):

        header = ((30-len(self.name))//2)*"*" + self.name + ((30-len(self.name))//2)*"*"
        return_value = header + '\n'
        for item in self.ledger:
            right_align_value = 30 - len(item["description"][:23])
            right_align_value = "{:>"+str(right_align_value)+"}"
            return_value += '{:<0}'.format(item["description"][:23]) + right_align_value.format(str("%.2f" % item["amount"])[:7]) + '\n'
        return_value += "Total: " + "%.2f" % self.get_balance()
        return return_value


def create_spend_chart(categories):
    n = 0
    for cat in categories:
        if len(cat.name) > n:
            n = len(cat.name)
    for i in range(len(categories)):
        if len(categories[i].name) < n:
            categories[i].name += " "*(n - len(categories[i].name))
    chart = ""
    header = "Percentage spent by category\n"
    bars = ""
    names = ""
    percentages = [0] * len(categories)
    total_spent = 0
    for i in range(len(categories)):
        for withdraw in categories[i].ledger:
            if withdraw["amount"] < 0:
                total_spent += withdraw["amount"]
                percentages[i] += withdraw["amount"]
    for i in range(len(percentages)):
        percentages[i] = int(round((percentages[i]/total_spent)/1, 2)*10)
        percentages[i] *= 10
    for i in range(11):
        bars += str((10-i)*10).rjust(3) + "|"
        for item in percentages:
            if item >=(10-i)*10:
                bars += " o "
            else:
                bars += "   "
        bars += ' \n'
    bars += "    " + "-"*(3*len(percentages)+1) + '\n'
    for i in range(n):
        names += "     "
        for j in range(len(categories)):
            names += categories[j].name[i] + "  "
        names += '\n'
    chart = (header + bars + names).rstrip('\n')
    return chart
