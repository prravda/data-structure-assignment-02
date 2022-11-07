from typing import Optional


class Node:
    def __init__(
            self,
            data: str,
            left: Optional['Node'] = None,
            right: Optional['Node'] = None,
    ):
        self.data = data
        self.left = left
        self.right = right
