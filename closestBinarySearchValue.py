Closest is either the root's value (a) or the closest in the appropriate subtree (b).

def closestValue(self, root, target):
    a = root.val
    kid = root.left if target < a else root.right
    if not kid: return a
    b = self.closestValue(kid, target)
    return min((b, a), key=lambda x: abs(target - x))
Alternative endings:

    return (b, a)[abs(a - target) < abs(b - target)]
    return a if abs(a - target) < abs(b - target) else b
    erative
Walk the path down the tree close to the target, return the closest value on the path. Inspired by yd, I wrote these after reading "while loop".

Python

def closestValue(self, root, target):
    path = []
    while root:
        path += root.val,
        root = root.left if target < root.val else root.right
    return min(path[::-1], key=lambda x: abs(target - x))
The [::-1] is only for handling targets much larger than 32-bit integer range, where different path values x have the same "distance" (x - target).abs. In such cases, the leaf value is the correct answer. If such large targets aren't asked, then it's unnecessary.

Or with O(1) space:

def closestValue(self, root, target):
    closest = root.val
    while root:
        closest = min((root.val, closest), key=lambda x: abs(target - x))
        root = root.left if target < root.val else root.right
    return closest