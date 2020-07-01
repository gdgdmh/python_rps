#!/usr/bin/env python
"""エントリーポイント."""

from rock_paper_scissors import man_player


def main():
    """エントリーポイント."""
    print('main')
    man = man_player.ManPlayer()
    man.start_showdown()
    print(man.get())


if __name__ == '__main__':
    main()
