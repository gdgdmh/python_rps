#!/usr/bin/env python
"""ジャンケンの手ジャッジクラス."""
from rock_paper_scissors import judge
from rock_paper_scissors import players
from rock_paper_scissors import hand_constant
from rock_paper_scissors import result_constant
from typing import Tuple, List


class StandardJudge(judge.Judge):
    """ジャンケンの手ジャッジクラス."""

    HAND_TYPE_COUNT = 3
    INDEX_ROCK = 0
    INDEX_PAPER = 1
    INDEX_SCISSORS = 2

    def __init__(self):
        """コンストラクタ."""
        self.__players = None

    def set(self, ps: players.Players):
        """判定のためにプレイヤーを設定."""
        if str(type(ps)) != "<class 'rock_paper_scissors.players.Players'>":
            raise ValueError("players not rock_paper_scissors.players.Players")
        self.__players = ps

    def judge(self) -> List[Tuple[int, List[int]]]:
        """設定されたジャンケンの手を判定して勝敗とplayerのindexを返す.DRAWの場合はindexは0."""
        if self.__players.length() <= 1:
            raise ValueError("players length <= 1. set player length >= 2")

        # あいこ
        if self._check_draw_three_hand(self.__players):
            return (result_constant.ResultConstant.DRAW, 0)
        if self._check_draw_same_hand(self.__players):
            return (result_constant.ResultConstant.DRAW, 0)
        # 勝敗
        count = self._get_count(self.__players)
        win_hand = self._get_win_hand(count)
        result = self._create_win_result_info(win_hand, self.__players)
        return result

    def _get_count(self, p: players.Players) -> List[Tuple[int, int, int]]:
        """手ごとのcountを取得する(rock, paper, scissors)."""
        rock_count = 0
        paper_count = 0
        scissors_count = 0
        for i in range(p.length()):
            h = p.get_hand(i)
            if h == hand_constant.HandConstant.ROCK:
                rock_count = rock_count + 1
            if h == hand_constant.HandConstant.PAPER:
                paper_count = paper_count + 1
            if h == hand_constant.HandConstant.SCISSORS:
                scissors_count = scissors_count + 1
        return (rock_count, paper_count, scissors_count)

    def _get_win_hand(self, hand_count: List[Tuple[int, int, int]]) -> int:
        """手のカウントから勝ちになる手を取得."""
        if hand_count[self.INDEX_ROCK] > 0:
            if hand_count[self.INDEX_SCISSORS] > 0:
                return hand_constant.HandConstant.ROCK
            if hand_count[self.INDEX_PAPER] > 0:
                return hand_constant.HandConstant.PAPER
        if hand_count[self.INDEX_PAPER] > 0:
            if hand_count[self.INDEX_SCISSORS] > 0:
                return hand_constant.HandConstant.SCISSORS
        assert False
        return hand_constant.HandConstant.ROCK

    def _get_player_index_by_hand(self, players: players.Players, hand: int):
        """指定された手を出しているプレイヤーindexをlistで取得."""
        count = players.length()
        counts = []
        for i in range(count):
            h = players.get_hand(i)
            if h == hand:
                counts.append(i)
        return counts

    def _create_win_result_info(self, h: int, ps: players.Players) \
            -> List[Tuple[int, int]]:
        """手から勝ちの結果情報を作成する."""
        return (result_constant.ResultConstant.WIN,
                self._get_player_index_by_hand(ps, h))

    def _check_result(self, hand1: int, hand2: int) -> List[Tuple[int, int]]:
        """ジャンケンの手で勝敗をチェックする(result, win(0 or 1))."""
        result = result_constant.ResultConstant.DRAW
        if hand1 == hand_constant.HandConstant.ROCK:
            result = self._check_result_rock(hand2)
        elif hand1 == hand_constant.HandConstant.PAPER:
            result = self._check_result_paper(hand2)
        elif hand1 == hand_constant.HandConstant.SCISSORS:
            result = self._check_result_scissors(hand2)

        if result == result_constant.ResultConstant.DRAW:
            return (result, 0)
        if result == result_constant.ResultConstant.WIN:
            return (result_constant.ResultConstant.WIN, 0)
        return (result_constant.ResultConstant.WIN, 1)

    def _check_result_rock(self, target_hand: int) -> int:
        """グーだった時の勝敗チェック."""
        if target_hand == hand_constant.HandConstant.ROCK:
            return result_constant.ResultConstant.DRAW
        if target_hand == hand_constant.HandConstant.PAPER:
            return result_constant.ResultConstant.LOSE
        if target_hand == hand_constant.HandConstant.SCISSORS:
            return result_constant.ResultConstant.WIN
        return result_constant.ResultConstant.DRAW

    def _check_result_paper(self, target_hand: int) -> int:
        """パーだった時の勝敗チェック."""
        if target_hand == hand_constant.HandConstant.ROCK:
            return result_constant.ResultConstant.WIN
        if target_hand == hand_constant.HandConstant.PAPER:
            return result_constant.ResultConstant.DRAW
        if target_hand == hand_constant.HandConstant.SCISSORS:
            return result_constant.ResultConstant.LOSE
        return result_constant.ResultConstant.DRAW

    def _check_result_scissors(self, target_hand: int) -> int:
        """チョキだった時の勝敗チェック."""
        if target_hand == hand_constant.HandConstant.ROCK:
            return result_constant.ResultConstant.LOSE
        if target_hand == hand_constant.HandConstant.PAPER:
            return result_constant.ResultConstant.WIN
        if target_hand == hand_constant.HandConstant.SCISSORS:
            return result_constant.ResultConstant.DRAW
        return result_constant.ResultConstant.DRAW

    def _check_draw_three_hand(self, players: players.Players):
        """あいこのチェック(3種)."""
        count = players.length()
        if count < StandardJudge.HAND_TYPE_COUNT:
            return False
        rock_found = False
        paper_found = False
        scissors_found = False
        for i in range(count):
            h = players.get_hand(i)
            if h == hand_constant.HandConstant.ROCK:
                rock_found = True
            elif h == hand_constant.HandConstant.PAPER:
                paper_found = True
            elif h == hand_constant.HandConstant.SCISSORS:
                scissors_found = True
            # all type found
            if rock_found and paper_found and scissors_found:
                return True
        return False

    def _check_draw_same_hand(self, players: players.Players):
        """あいこのチェック(同じ手)."""
        hand_type = None
        count = players.length()
        if count < 2:
            return False
        hand_type = players.get_hand(0)
        for i in range(count):
            h = players.get_hand(i)
            if h != hand_type:
                return False
        return True
