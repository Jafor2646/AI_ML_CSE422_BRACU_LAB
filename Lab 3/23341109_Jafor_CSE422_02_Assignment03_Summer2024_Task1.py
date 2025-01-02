import random

def minimax(depth, node_index, is_maximizing_player, leaf, alpha, beta):
    if depth == 5:
        return leaf[node_index]

    if is_maximizing_player:
        max_eval = float('-inf')
        for i in range(2): 
            eval = minimax(depth + 1, node_index * 2 + i, False, leaf, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):  
            eval = minimax(depth + 1, node_index * 2 + i, True, leaf, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval



inp = open("23341109_Jafor_CSE422_02_Assignment03_Summer2024_inputFile1.txt", "r")
out = open("output1.txt", "w")
leaf = [random.choice([-1, 1]) for _ in range(32)]
starting_player = int(inp.readline())
winner = []
for i in range(3):
  round_winner = minimax(0, 0, starting_player == 0, leaf, float('-inf'), float('inf'))
  if round_winner == -1:
      winner.append("Scorpion")
  else:
      winner.append("Sub-Zero")
  if starting_player == 0:
      starting_player = 1
  else:
      starting_player = 0
    

out.write(f"Game Winner: {max(winner)}\n")
out.write(f"Total Rounds Played: 3\n")
for i in range(3):
    out.write(f"Winner of Round {i+1}: {winner[i]}\n")

