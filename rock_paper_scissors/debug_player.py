#!/usr/bin/env python
"""デバッグ用プレイヤークラス."""
from rock_paper_scissors import player
from rock_paper_scissors import hand_constant


class DebugPlayer(player.Player):
    """デバッグ用プレイヤークラス."""

    def __init__(self):
        """コンストラクタ."""
        self.__hand = hand_constant.HandConstant.ROCK

    def start_showdown(self):
        """手の公開の前に呼ばれる."""

    def get(self) -> int:
        """手の公開."""
        return self.__hand

    def set(self, hand: int):
        """手の設定."""
        self.__hand = hand
