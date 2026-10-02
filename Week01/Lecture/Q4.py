top_scorers = [
      ["11 goal(s)", "Sebastien Haller", "Ajax"],
      ["8 goal(s)", "Mohamed Salah", "Liverpool"],
      ["14 goal(s)", "Karim Benzema", "Real Madrid"],
      ["7 goal(s)", "Christopher Nkunku", "Leipzig"],
      ["14 goal(s)", "Robert Lewandowski", "Bayern Munich"]
]

goals = []
for elem in top_scorers:
    goal = int(elem[0].replace(" goal(s)", ""))
    goals.append(goal)
maxVal = max(goals)

for elem in top_scorers:
    goal = int(elem[0].replace(" goal(s)", ""))
    if goal == maxVal:
        print(elem[1], "-", elem[2])
