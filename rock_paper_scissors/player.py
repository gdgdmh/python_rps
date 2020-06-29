#!/usr/bin/env python
"""ジャンケンのプレイヤーインターフェース."""
from abc import ABCMeta, abstractmethod

from rock_paper_scissors import hand_constant


class Player(metaclass=ABCMeta):
    """ジャンケンのプレイヤーインターフェース."""

    @abstractmethod
    def start_showdown(self):
        """手の公開の前に呼ばれる."""
        pass

    @abstractmethod
    def get(self) -> int:
        """手の公開."""
        return hand_constant.HandConstant.ROCK
