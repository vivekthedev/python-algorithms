def is_sorted(node):
    if node is None:
        return (None, True)
    left_value, left_sorted = is_sorted(node.left)
    if (left_sorted is False) or (left_value and left_value > node.val):
        return (None, False)
    right_value, right_sorted = is_sorted(node.right)
    if (right_sorted is False) or (right_value is not None and right_value < node.val):
        return (None, False)
    return (node.val, True)
