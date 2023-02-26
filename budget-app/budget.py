class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, "description" : description})

  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": amount * -1, "description": description})
      return True
    return False

  def get_balance(self):
    balance  = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, category_object):
    if self.check_funds(amount):
      self.withdraw(amount, description=f"Transfer to {category_object.name}")
      category_object.deposit(amount, description=f"Transfer from {self.name}")
      return True
    return False

  def check_funds(self, amount):
    balance = self.get_balance()
    if balance == 0 or balance < amount:
      return False
    return True

  def __repr__(self):
    star_lenght = (30 - len(self.name)) // 2
    spent = []
    title = '*' * star_lenght + self.name + '*' * star_lenght
    spent.append(title)
    for item in self.ledger:
      amount = ' ' * (7-len(f'{item["amount"]:.2f}')) + f'{item["amount"]:.2f}'
      if len(item["description"]) >= 23:
        description = item["description"][:23]
      else:
        description = item['description'] + ' ' * (23-len(item['description']))
      spent.append(description + amount)
    total = f'Total: {self.get_balance():.2f}'
    spent.append(total)
    return '\n'.join(spent)


def create_spend_chart(categories):
  total = 0
  withdrawl_list = []
  for category in categories:
    withdrawn_amount = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total += (item['amount'] * -1)
        withdrawn_amount += (item['amount'] * -1)
    withdrawl_list.append([category.name, withdrawn_amount])
  percentage_withdrawn = []
  for item in withdrawl_list:
    percentage_withdrawn.append([item[0], (item[1]/total) * 100])
  category_names = [item[0] for item in percentage_withdrawn]
  category_name_lengths = [len(name) for name in category_names]
  percentages = [item[1] for item in percentage_withdrawn]
  chart = "Percentage spent by category"
  for i in range(100, -1, -10):
    chart += '\n' + str(i).rjust(3) + '|'
    for percentage in percentages:
      if percentage > i:
        chart += ' o '
      else:
        chart += '   '
    chart += ' '
  chart += '\n    ----------'
  max_length = max(category_name_lengths)
  for i in range(max_length):
    chart += '\n    '
    for j in range(len(category_names)):
      if i < category_name_lengths[j]:
        chart += ' ' + category_names[j][i] + ' '
      else:
        chart += '   '
    chart += ' '
  return chart