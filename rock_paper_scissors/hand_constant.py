#!/usr/bin/env python
"""ジャンケンの手の定数クラス."""


class HandConstant():
    """ジャンケンの手の定数クラス."""

    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    __ROCK_NAME = "rock"
    __PAPER_NAME = "paper"
    __SCISSORS_NAME = "scissors"

    @staticmethod
    def get_name(type: int) -> str:
        """名前を取得する."""
        if type == HandConstant.ROCK:
            return HandConstant.__ROCK_NAME
        if type == HandConstant.PAPER:
            return HandConstant.__PAPER_NAME
        if type == HandConstant.SCISSORS:
            return HandConstant.__SCISSORS_NAME
        return ""

    @staticmethod
    def check_hand(target_hand: int) -> bool:
        """手の正常性を確認する."""
        if (target_hand == HandConstant.ROCK
                or target_hand == HandConstant.PAPER
                or target_hand == HandConstant.SCISSORS):
            return True
        return False
