import empirical

solver = empirical.Solver()

dataset = [64, 81, 49, 25]
solutions = []
for problem in dataset:
  solutions.append(solver.solve(*problem))

answers = [8, 9, 7, 5]
correct_count = 0
for i in xrange(len(dataset)):
  if solutions[i] == answers[i]:
  	correct_count = correct_count + 1

accuracy = correct_count / len(dataset)

results = {
  'overall': {
    'type': 'table',
    'metric': 'Accuracy',
    'value': accuracy
  }
}
empirical.postResults(results)