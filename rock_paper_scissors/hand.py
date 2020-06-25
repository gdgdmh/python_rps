#!/usr/bin/env python
"""ジャンケンの手インターフェース."""
from abc import ABCMeta, abstractmethod

from rock_paper_scissors import hand_constant


class Hand(metaclass=ABCMeta):
    """ジャンケンの手インターフェース."""

    @abstractmethod
    def get_type(self):
        """ジャンケンの手のタイプを取得する."""
        return hand_constant.HandConstant.ROCK

    @abstractmethod
    def get_name(self):
        """名前を取得する."""
        return "hand"
