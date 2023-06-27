def successor(root):
    if root.right == None:
        given = root.value
        root = root.parent
        while root.value < given:
            if root.parent == None:
                return None
            root = root.parent
    else:
        root = root.right
        while root.left != None:
            root = root.left
    return root
