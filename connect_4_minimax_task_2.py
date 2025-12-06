# الكلاس ده بس ماسك النود في الشجرة
class TreeNode:
    def __init__(self, col=None, value=None):
        self.col = col      # العمود اللي اتجرب
        self.value = value  # القيمة اللي minimax رجّعها
        self.children = []  # فروع النود

#علشان اعرف عمل كام حالة
class Stats:
    def __init__(self):
        self.nodes = 0
#دي علشان اطبع التري
def print_tree(node, level=0):
    if node is None:
        return
    print("    " * level + f"col={node.col}, val={node.value}")
    for ch in node.children:
        print_tree(ch, level + 1)

#MINIMAX
def minimax(board, depth, maximizing, game, stats, node):
    stats.nodes += 1  # كل ما نزور حالة نزود العداد

    # لو وصلنا للعمق أو اللعبة خلصت خلاص
    if depth == 0 or game.is_terminal(board):
        val = game.score_position(board)
        node.value = val
        return val

    valid_cols = game.get_valid_locations(board)

    if maximizing:
        best = -999999
        for col in valid_cols:
            temp = game.make_move(board, col, game.AI)
            child = TreeNode(col)
            node.children.append(child)
            val = minimax(temp, depth - 1, False, game, stats, child)
            if val > best:
                best = val
        node.value = best
        return best
    else:
        best = 999999
        for col in valid_cols:
            temp = game.make_move(board, col, game.PLAYER)
            child = TreeNode(col)
            node.children.append(child)
            val = minimax(temp, depth - 1, True, game, stats, child)
            if val < best:
                best = val
        node.value = best
        return best

#ALPHA-BETA  
def alphabeta(board, depth, alpha, beta, maximizing, game, stats, node):
    stats.nodes += 1

    if depth == 0 or game.is_terminal(board):
        val = game.score_position(board)
        node.value = val
        return val

    valid_cols = game.get_valid_locations(board)

    if maximizing:
        best = -999999
        for col in valid_cols:
            temp = game.make_move(board, col, game.AI)
            child = TreeNode(col)
            node.children.append(child)
            val = alphabeta(temp, depth - 1, alpha, beta, False, game, stats, child)
            if val > best:
                best = val
            alpha = max(alpha, val)
            if alpha >= beta:   # purring
                break
        node.value = best
        return best
    else:
        best = 999999
        for col in valid_cols:
            temp = game.make_move(board, col, game.PLAYER)
            child = TreeNode(col)
            node.children.append(child)
            val = alphabeta(temp, depth - 1, alpha, beta, True, game, stats, child)
            if val < best:
                best = val
            beta = min(beta, val)
            if alpha >= beta:   # purring
                break
        node.value = best
        return best

# دي دالة بترجع أفضل حركة
def get_ai_move(board, depth, game, use_ab=True):
    stats = Stats()
    root = TreeNode()
    valid_cols = game.get_valid_locations(board)

    best_col = None
    best_val = -999999

    for col in valid_cols:
        new_board = game.make_move(board, col, game.AI)
        child = TreeNode(col)
        root.children.append(child)

        if use_ab:
            val = alphabeta(new_board, depth - 1, -999999, 999999, False, game, stats, child)
        else:
            val = minimax(new_board, depth - 1, False, game, stats, child)

        if val > best_val:
            best_val = val
            best_col = col

    print("--- AI Tree ---")
    print_tree(root)
    print(f"Nodes expanded: {stats.nodes}")

    return best_col
