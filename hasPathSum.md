Need to be concise even for the logic
The key is for the leaf return true or not
on consider one approach onetime, don't mess up with other approach to do another catetory: for edge case with only one child, should return false only
 if root == None: return False  #make simplize
            # if sum == 0:
            #     return True
            # else: return False
        elif  root.left == None and root.right == None:
            return sum == root.val 
   