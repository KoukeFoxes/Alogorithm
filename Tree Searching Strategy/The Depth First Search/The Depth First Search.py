class Tree(object):
    
    def __init__(self, data):
        self.data = data
        self.children = list()

def deep_first_search(tree, target):
    if tree.data == target:
        return True
    for child in tree.children:
        if deep_first_search(child, target):
            return True
    return False

if __name__ == '__main__':
    
    #add node to tree
    tree = Tree('7')
    tree.children = [Tree('5'), Tree('1'), Tree('2')]
    tree.children[1].children = [Tree('2'), Tree('10')]
    
    #looking for 10
    print(deep_first_search(tree, '100'))