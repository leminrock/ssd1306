def forward_routine(_status):
    item = _status.current

    if item.children[0]:
        _status.previous = item
        _status.current = item.children[0]


def backward_routine(_status):
    item = _status.current

    if item.parent:
        _status.previous = item
        _status.current = item.parent
