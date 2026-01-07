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
def invertTree(root: TreeNode) -> TreeNode:
    #Complexity o(N): because it goes through each node Once
    # Base case
    if not root:
        return None
    # Swap the children
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root
def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if not root:
        return False
    # If  this is a leaf NODE - it does not have left and right
    if not root.left and not root.right:
        return targetSum == root.val
    new_sum = targetSum - root.val
    return hasPathSum(root.left, new_sum) or hasPathSum(root.right, new_sum)
# Level 3
floodlight = TreeNode("Floodlight")

# Level 2
camera = TreeNode("Camera", left=floodlight)
chime = TreeNode("Chime")

# Level 1 (Root)
root = TreeNode("Doorbell", left=camera, right=chime)
#print(maxDepth(root))

# Create: 1 -> (Left: 2, Right: 3)
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
print(hasPathSum(root2, 3))
print(root2.left.val)  # Expected: Chime
print(root2.right.val) # Expected: Camera
inverted = invertTree(root2)


print(inverted.left.val)  # Expected: 3
print(inverted.right.val) # Expected: 2
