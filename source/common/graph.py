import networkx as nx

def init():
    "create main graph"
    global GRAPHMENU
    GRAPHMENU = nx.DiGraph()
    return None

def add_node(item):
    """add a node in the graph"""
    global GRAPHMENU
    GRAPHMENU.add_node(item)

def add_nodes(items):
    """add list of nodes in the graph"""
    global GRAPHMENU
    GRAPHMENU.add_nodes_from(items)


def add_child(parent, child):
    """add a child starting from a node"""
    global GRAPHMENU
    GRAPHMENU.add_edge(parent, child)


def add_children(parent, children: list):
    """add a list of nodes starting from a node"""
    global GRAPHMENU
    for child in children:
        add_child(parent, child)


def get_children(node):
    """get children list of a node"""
    global GRAPHMENU
    return GRAPHMENU.successors(node)


def get_parent(node):
    """get parent of a node"""
    global GRAPHMENU
    pre = list(GRAPHMENU.predecessors(node))
    
    if pre:
        return pre[0]

    return None

