#!/usr/bin/env python
"""ジャンケンの手ジャッジインターフェース."""
from abc import ABCMeta, abstractmethod

from rock_paper_scissors import hand
from rock_paper_scissors import result_constant


class Judge(metaclass=ABCMeta):
    """ジャンケンの手ジャッジインターフェース."""

    @abstractmethod
    def set(self, hands: hand.Hand):
        """判定のための手を設定."""
        pass

    @abstractmethod
    def judge(self) -> (int, int):
        """設定されたジャンケンの手を判定して勝敗とhandのindexを返す."""
        return (result_constant.ResultConstant.DRAW, 0)
