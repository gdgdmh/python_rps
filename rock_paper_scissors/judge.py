#!/usr/bin/env python
"""ジャンケンの手ジャッジインターフェース."""
from abc import ABCMeta, abstractmethod

from rock_paper_scissors import players
from rock_paper_scissors import result_constant


class Judge(metaclass=ABCMeta):
    """ジャンケンの手ジャッジインターフェース."""

    @abstractmethod
    def set(self, players: players.Players):
        """判定のためのプレイヤーを設定."""
        pass

    @abstractmethod
    def judge(self) -> (int, int):
        """設定されたジャンケンの手を判定して勝敗とhandのindexを返す."""
        return (result_constant.ResultConstant.DRAW, 0)
