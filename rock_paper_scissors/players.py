#!/usr/bin/env python
"""プレイヤーまとめクラス."""

from rock_paper_scissors import player


class Players():
    """プレイヤーまとめクラス."""

    def __init__(self):
        """コンストラクタ."""
        self.__players = []

    def add(self, add_player: player.Player):
        """プレイヤーの追加."""
        self.__players.append(add_player)

    def clear(self):
        """プレイヤーデータのクリア."""
        self.__players.clear()

    def length(self):
        """プレイヤーデータ数の取得."""
        return len(self.__players)

    def clone(self, source):
        """クローンを作成する."""
        self.__players.clear()
        for p in source.__players:
            self.__players.append(p)

    def get_hand(self, index) -> int:
        """プレイヤーの手の取得."""
        return self.__players[index].get()

    def get(self, index) -> player.Player:
        """プレイヤーの取得."""
        return self.__players[index]
