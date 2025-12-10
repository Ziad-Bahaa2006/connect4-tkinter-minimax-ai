from game_board import Connect4, AI, PLAYER, heuristic
import math

# كل نود بتمثل حركة (عمود) + القيمة اللي الـ AI حسبها للحركة دي
class TreeNode:
    def __init__(self, col=None, value=None):
        self.col = col        # العمود اللي النود دي بتمثل لعب فيه
        self.value = value    # قيمة التقييم بعد تنفيذ الحركة
        self.children = []    # أولاد النود (الحركات اللي بعد الحركة الحالية)

# كلاس بسيط لتجميع إحصائيات البحث
class Stats:
    def __init__(self):
        self.nodes = 0      
        self.total_nodes = 0  

def print_tree(node, level=0):
    if node is None: 
        return
    indent = "  " * level
    print(f"{indent}Col {node.col} → Value: {node.value}")
    for child in node.children:
        print_tree(child, level + 1)


def alphabeta(state: Connect4, depth, alpha, beta, maximizing, stats, node):

    stats.nodes += 1
    stats.total_nodes += 1

    if depth == 0 or state.terminal():
        val = heuristic(state, AI)  
        node.value = val       
        return val

    moves = state.valid_moves()  # الأعمدة اللي مازالت صالحة للعب

    
    if maximizing:
        best = -math.inf

        for col in moves:
            next_state = state.copy()           # ننسخ البورد عشان منغيرش الأصلي
            next_state.make_move(col, AI)       
            child = TreeNode(col)              
            node.children.append(child)

            val = alphabeta(next_state, depth-1, alpha, beta, False, stats, child)

            best = max(best, val)              
            alpha = max(alpha, val)             # نحدّث Alpha

            if alpha >= beta:
                break

        node.value = best
        return best


    else:
        best = math.inf

        for col in moves:
            next_state = state.copy()
            next_state.make_move(col, PLAYER)

            child = TreeNode(col)
            node.children.append(child)

            val = alphabeta(next_state, depth-1, alpha, beta, True, stats, child)

            best = min(best, val)
            beta = min(beta, val)

            if alpha >= beta:
                break

        node.value = best
        return best



# الدالة الأساسية اللي الـ main بيستدعيها
# وظيفتها:
# - تشغّل AlphaBeta على كل الأعمدة المتاحة
# - تختار العمود اللي جاب أفضل Score
# - ترجع العمود + إحصائيات البحث

def get_ai_move(board: Connect4, depth=5, print_debug=True):

    # لو مفيش حركات خالص
    if not board.valid_moves():
        return None, None

    stats = Stats()          # نبدأ الإحصائيات من صفر
    root = TreeNode()        
    best_col = None
    best_val = -math.inf

    if print_debug:
        print("\n" + "="*70)
        print(f"AI IS THINKING... (Depth = {depth})")
        print("="*70)

    # نجرّب كل عمود صالح للعب ونشوف أحسنهم
    for col in board.valid_moves():
        new_board = board.copy()
        new_board.make_move(col, AI)

        child = TreeNode(col)
        root.children.append(child)

        val = alphabeta(new_board, depth-1, -math.inf, math.inf, False, stats, child)

        # لو الحركة دي أحسن من اللي قبلها
        if val > best_val:
            best_val = val
            best_col = col

    if print_debug:
        print_tree(root)
        current_heuristic = heuristic(board, AI)
        print(f"\nHeuristic (AI perspective): {current_heuristic}")
        print(f"Nodes explored this move: {stats.nodes}")
        print(f"Total nodes explored in game: {stats.total_nodes}")
        print("-" * 70)

    return best_col, stats
