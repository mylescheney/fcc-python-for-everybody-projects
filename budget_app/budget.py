class Category :
    def __init__(self, category) :
        self.category = category
        self.ledger = list()

    def get_balance(self) :
        balance = 0
        for item in self.ledger :
            balance = balance + item["amount"]
        return(balance)

    def check_funds(self, amount) :
        balance = self.get_balance()
        if amount < 0 :
            amount = amount * -1
        if balance >= amount :
            return True
        else :
            return False

    def deposit(self, amount, description) :
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description) :
        if self.check_funds(amount) :
            if amount > 0 :
                amount = amount * -1
            self.ledger.append({"amount": amount, "description": description})
            return True
        else :
            return False   

    def transfer(self, amount, other_category) :
        if self.check_funds(amount) :
            if amount > 0 :
                amount = amount * -1
            self.withdraw(amount, "Transfer to " + other_category.category)
            amount = amount * -1
            other_category.deposit(amount, "Transfer from " + self.category)
            return True
        else :
            return False

    def print_category(self) :
        nStarsLeft = int()
        starsLeft = str()
        nStarsRight = int()
        starsRight = str()
        if len(self.category) % 2 != 0 :
            nStarsLeft = int((30 - len(self.category)) / 2 + 0.5)
            nStarsRight = int((30 - len(self.category)) / 2)
        else :
            nStarsLeft = int((30 - len(self.category)) / 2)
            nStarsRight = int((30 - len(self.category)) / 2)
        for star in range(nStarsLeft) :
            starsLeft = starsLeft + "*"
        for star in range(nStarsRight) :
            starsRight = starsRight + "*"
        header = starsLeft + self.category + starsRight + "\n"

        ledger_str = str()
        for item in self.ledger :
            description = item["description"]
            if len(description) >= 23 :
                description = description[0:23]
            else :
                spaces = 23 - len(description)
                for space in range(spaces) :
                    description = description + " "
            
            amount_str = str(item["amount"])
            if len(amount_str) >= 7 :
                amount_str = amount_str[0:7]
            else :
                spaces = 7 - len(amount_str)
                for space in range(spaces) :
                    amount_str = " " + amount_str
            ledger_str = ledger_str + description + amount_str + "\n"
        
        total_str = "Total: " + str(self.get_balance())

        return header + ledger_str + total_str

def create_spend_chart(categories) :
    total_spent = 0
    for category in categories :
        withdrawels = 0
        for item in category.ledger :
            if item["amount"] < 0 :
                withdrawels = withdrawels + item["amount"]
        total_spent = total_spent + withdrawels

    chart = str()

    percentages = list()
    for category in categories :
        withdrawels = 0
        for item in category.ledger :
            if item["amount"] < 0 :
                withdrawels = withdrawels + item["amount"]
        percentage = round((withdrawels / total_spent) * 10)
        if percentage < 10 :
            spaces = 10 - percentage
            percentage_str = str()
            for space in range(spaces) :
                percentage_str = " " + percentage_str
            for x in range(percentage) :
                percentage_str = percentage_str + "o"
            percentages.append(percentage_str + "o")
        else :
            percentages.append('ooooooooooo')

    y_marker = 100
    for x in range(11) :
        y_marker_str = str(y_marker) + "| "
        if len(y_marker_str) < 5 :
            spaces = 5 - len(y_marker_str)
            for space in range(spaces) :
                y_marker_str = " " + y_marker_str
        circles = str()
        for z in percentages :
            circles = circles + z[x] + "  "
        chart = chart + y_marker_str + circles + "\n"
        y_marker = y_marker - 10

    x_axis = '-'
    for category in categories :
        x_axis = x_axis + "---"
    chart = chart + "    " + x_axis + "\n     "

    vertical_categories = str()
    all_category_names = list()
    longest_name = int()
    for category in categories :
        all_category_names.append(category.category)
        if longest_name == None or longest_name < len(category.category) :
            longest_name = len(category.category)
    x = 0
    while x < longest_name :
        y = 0
        while y < len(all_category_names) :

            if y < len(all_category_names) - 1 :
                if len(all_category_names[y]) > x :
                    vertical_categories = vertical_categories + all_category_names[y][x] + "  "
                else :
                    vertical_categories = vertical_categories + "   "
            else :
                if len(all_category_names[y]) > x :
                    vertical_categories = vertical_categories + all_category_names[y][x] + "  \n     "
                else :
                    vertical_categories = vertical_categories + "   \n     "


            y = y + 1
        x = x + 1
    chart = chart + vertical_categories
    return chart

t1 = Category('Spending')
t2 = Category('Groceries')
t1.deposit(1000, "Test deposit")
t1.withdraw(1000, "Long description of lots of things test")
t2.deposit(10000, "Test deposit")
t2.withdraw(5000, "Long description of lots of things test")

print(create_spend_chart([t1, t2]))