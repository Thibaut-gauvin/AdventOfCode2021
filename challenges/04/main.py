from typing import List

CHECK_MARK = "x"
UNCHECK_MARK = "."


class Card:
    def __init__(self):
        self._card_content = []
        self._bingo = [
            [UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK],
            [UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK],
            [UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK],
            [UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK],
            [UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK, UNCHECK_MARK],
        ]

    def get_content(self) -> List:
        return self._card_content

    def add_row(self, row_content: List[int]) -> None:
        self._card_content.append(row_content)

    def compute(self, draw_entry: int):
        for x in range(len(self._card_content)):
            for y in range(len(self._card_content[x])):
                if self._card_content[x][y] == draw_entry:
                    self._bingo[x][y] = CHECK_MARK
        return self

    def check_win(self) -> bool:
        for index in range(len(self.get_content())):
            if self._bingo[index].count(CHECK_MARK) == 5:
                return True
            if [row[index] for row in self._bingo].count(CHECK_MARK) == 5:
                return True
        return False

    def get_score(self, figure: int) -> int:
        unchecked_figure = []
        for x in range(len(self._bingo)):
            for y in range(len(self._bingo)):
                if self._bingo[x][y] == UNCHECK_MARK:
                    unchecked_figure.append(int(self._card_content[x][y]))
        print("unchecked_figure: %s" % unchecked_figure)
        return sum(unchecked_figure) * figure

    def __str__(self) -> str:
        return "%s\n\n%s" % (
            '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self._card_content]),
            '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self._bingo]),
        )


class Game:
    def __init__(self, boards: List[Card]):
        self._cards = boards

    def get_cards(self) -> List[Card]:
        return self._cards


def parse_puzzle_input() -> (int, List[Card]):
    player_boards = []
    card: Card = Card()
    with open('input.txt', 'r') as file:
        for line in file:
            current_line = line.strip()
            if line.find(',') != -1:
                draw = list(map(int, current_line.split(",")))
            else:
                if current_line == "":
                    if len(card.get_content()) == 5:
                        player_boards.append(card)
                        card = Card()
                    continue
                board_line = list(map(int, " ".join(current_line.split()).split(" ")))
                card.add_row(board_line)
        return draw, player_boards


def part_1():
    print("=== init game ===")
    draw_entries, player_boards = parse_puzzle_input()
    game = Game(player_boards)

    print("=== start game ===")
    for figure in draw_entries:
        print("=== current figure: %s ===" % figure)
        for card in game.get_cards():
            card.compute(figure)
            if card.check_win() is True:
                print("=== Found a winning Card !")
                print(card)
                print(card.get_score(figure))
                exit(0)

    print("=== game ended ===")


def part_2():
    draw_entries, player_boards = parse_puzzle_input()
    game = Game(player_boards)

    remaining = game.get_cards()
    for figure in draw_entries:
        print("=== current figure: %s ===" % figure)
        computed = list(map(lambda card: card.compute(figure), remaining))
        wining_boards = list(filter(lambda card: card.check_win() is True, computed))
        for board in wining_boards:
            remaining.remove(board)
            if len(remaining) == 0:
                print(board.get_score(figure))
                print("expected: 148 * 13 = 1924")
                exit(0)


if __name__ == "__main__":
    # part_1()
    part_2()
