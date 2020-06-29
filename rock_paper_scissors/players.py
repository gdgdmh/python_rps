#!/usr/bin/env python
"""プレイヤーまとめクラス."""

from rock_paper_scissors import player


class Players():
    """プレイヤーまとめクラス."""

    def __init__(self):
        """コンストラクタ."""
        self.__players = []

    def add(self, add_player: player):
        """プレイヤーの追加."""
        self.__players.append(add_player)

    def clear(self):
        """プレイヤーデータのクリア."""
        self.__players.clear()

    def length(self):
        """プレイヤーデータ数の取得."""
        return len(self.__players)
