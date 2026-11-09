import lunch_card as l

alice = l.LunchCard(1, "Alice", 100)
bob = l.LunchCard(2, "Bob")

alice.DisplayCurrentBalance()
bob.DisplayCurrentBalance()

alice.payLunch(70)
alice.payLunch(20)
alice.payLunch(30)
alice.depositMoney(200)
alice.payLunch(40)

bob.depositMoney(500)
bob.payLunch(200)
bob.DisplayCurrentBalance()