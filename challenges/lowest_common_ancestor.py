from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    current = root

    while current is not None:
        current_value = current.get_value()

        if value1 < current_value and value2 < current_value:
            current = current.get_left_child()
        elif value1 > current_value and value2 > current_value:
            current = current.get_right_child()
        else:
            return current_value

    raise ValueError("Values are not present in the tree")
