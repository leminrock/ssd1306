import networkx as nx

GRAPHMENU = None


def init():
    """create main graph"""
    global GRAPHMENU
    GRAPHMENU = nx.DiGraph()
    return None


def add_node():
    """add a node in the graph"""
    pass


def add_child():
    """add a child starting from a node"""
    pass


def add_children():
    """add a list of nodes starting from a node"""
    pass


def get_children():
    """get children list of a node"""
    pass


def get_parent():
    """get parent of a node"""
    pass
