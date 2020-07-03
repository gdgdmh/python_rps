#!/usr/bin/env python
"""エントリーポイント."""

from rock_paper_scissors import players
#  from rock_paper_scissors import man_player
from rock_paper_scissors import cpu_player
from rock_paper_scissors import rock_paper_scissors


def main():
    """エントリーポイント."""
    print('main')
    rps = rock_paper_scissors.RockPaperScissors()
    ps = players.Players()
    ps.add(cpu_player.CpuPlayer())
    ps.add(cpu_player.CpuPlayer())
    rps.initialize_game(ps)

    while not rps.is_finished():
        rps.task()


if __name__ == '__main__':
    main()
