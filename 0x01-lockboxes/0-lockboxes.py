#!/usr/bin/python3
"""Lockboxes.

* You have n number of locked boxes in front of you.
  Each box is numbered sequentially from 0 to n - 1
  and each box may contain keys to the other boxes.

* Write a method that determines if all the boxes can be opened.

  * Prototype: def canUnlockAll(boxes)
  * boxes is a list of lists
  * A key with the same number as a box opens that box
  * You can assume all keys will be positive integers
    * There can be keys that do not have boxes
  * The first box boxes[0] is unlocked
  * Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened.

    Args:
        boxes (list): list of boxes with a nested list of keys

    Returns:
        True if all boxes can be opened, else return False
    """
    if type(boxes) is not list:
        return False
    _max = len(boxes)
    _boxes = set(range(_max))

    def unlock_box(key):
        """Check a box that belongs to the key provided."""
        if key >= _max:
            return
        _boxes.remove(key)
        for newkey in boxes[key]:
            if newkey in _boxes:
                unlock_box(newkey)
    if _max > 0:
        unlock_box(0)
    return len(_boxes) == 0

