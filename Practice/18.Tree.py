class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def maxDepth(root: TreeNode) -> int:
    # Base case: with if the root is None?
    if not root:
        return 0
    # 2. Recursive step:
    # Get the depth of the left side
    left_side = maxDepth(root.left)
    # Get the depth of the right side
    right_side = maxDepth(root.right)
    # Return 1 + larger of 2 sides
    return 1 + max(left_side, right_side)
# Level 3
floodlight = TreeNode("Floodlight")

# Level 2
camera = TreeNode("Camera", left=floodlight)
chime = TreeNode("Chime")

# Level 1 (Root)
root = TreeNode("Doorbell", left=camera, right=chime)
print(maxDepth(root))
