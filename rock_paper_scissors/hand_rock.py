#!/usr/bin/env python
"""ジャンケンの手グー."""
from rock_paper_scissors import hand
from rock_paper_scissors import hand_constant


class HandRock(hand.Hand):
    """ジャンケンの手グー."""

    def __init__(self):
        """コンストラクタ."""
        self.__type = hand_constant.HandConstant.ROCK
        pass

    def get_type(self):
        """ジャンケンの手のタイプを取得する."""
        return self.__type

    def get_name(self):
        """名前を取得する."""
        return hand_constant.HandConstant.get_name(self.__type)
