def best_split(X, y):
    best_gini, split = 1.0, (0, 0)
    for col in range(len(X[0])):
        for row in X:
            thr = row[col]
            l = [yi for xi, yi in zip(X, y) if xi[col] <= thr]
            r = [yi for xi, yi in zip(X, y) if xi[col] > thr]
            if not l or not r: continue
            g = sum((len(g_y)/len(y))*(1 - sum((g_y.count(c)/len(g_y))**2 for c in set(g_y))) for g_y in (l, r))
            if g < best_gini: best_gini, split = g, (col, thr)
    return split

if __name__ == "__main__":
    assert best_split([[1], [2], [8], [9]], [0, 0, 1, 1]) == (0, 2)
    print("[PASS] 088_decision_tree_cart")
