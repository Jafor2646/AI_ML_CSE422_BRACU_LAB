leaf_nodes = [3, 6, 2, 3, 7, 1, 2, 0]
def minimax(depth, node_index, is_maximizing_player):
        if depth == 3:
            return leaf_nodes[node_index]

        if is_maximizing_player:
            return max(minimax(depth + 1, node_index * 2, False), minimax(depth + 1, node_index * 2 + 1, False))
        else:
            return min(minimax(depth + 1, node_index * 2, True), minimax(depth + 1, node_index * 2 + 1, True))



inp = open("23341109_Jafor_CSE422_02_Assignment03_Summer2024_inputFile2.txt", "r")
out = open("output2.txt", "w")

c = int(inp.readline())
output = None
minimax_value_without_magic = minimax(0, 0, True)
left_subtree_value = max(leaf_nodes[0], leaf_nodes[1]) - c
right_subtree_value = max(leaf_nodes[4], leaf_nodes[5]) - c
minimax_value_with_magic = max(left_subtree_value, right_subtree_value)

if minimax_value_with_magic > minimax_value_without_magic:
    if right_subtree_value > left_subtree_value:
        output = f"The new minimax value is {minimax_value_with_magic}. Pacman goes right and uses dark magic\n"
    else:
        output = f"The new minimax value is {minimax_value_with_magic}. Pacman goes left and uses dark magic\n"
else:
    output = f"The minimax value is {minimax_value_without_magic}. Pacman does not use dark magic\n"

out.write(output)

