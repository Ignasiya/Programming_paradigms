import random


class GameBoard:
    __slots__ = "board"

    def __init__(self) -> None:
        self.board = [x for x in range(1, 10)]

    def __set__(self, symbol, position) -> None:
        self.board[position - 1] = symbol

    def view(self) -> None:
        print('\n┌', '—', '—', '—', '┐',
              '\n|', self.board[0], self.board[1], self.board[2], '|',
              '\n|', self.board[3], self.board[4], self.board[5], '|',
              '\n|', self.board[6], self.board[7], self.board[8], '|',
              '\n└', '—', '—', '—', '┘',
              sep=" ")

    def check_input(self) -> int:
        while True:
            try:
                key: int = int(input("введите позицию\n-> "))
                if key < 1 or key > 9:
                    raise Exception()
                elif not isinstance(self.board[key - 1], int):
                    raise Exception()
            except Exception:
                print("ОШИБКА: такой позиции нету или она занята")
                continue
            return key

    def both(self) -> int:
        number_list = list(filter(lambda x: type(x) is int, self.board))
        if len(number_list) > 0:
            return random.choice(number_list)
        else:
            return -1

    def is_win(self, symbol, text) -> bool:
        if (self.board[0] == self.board[1] == self.board[2] == symbol) \
                or (self.board[0] == self.board[3] == self.board[6] == symbol) \
                or (self.board[2] == self.board[5] == self.board[8] == symbol) \
                or (self.board[6] == self.board[7] == self.board[8] == symbol) \
                or (self.board[0] == self.board[4] == self.board[8] == symbol) \
                or (self.board[2] == self.board[4] == self.board[6] == symbol) \
                or (self.board[1] == self.board[4] == self.board[7] == symbol) \
                or (self.board[3] == self.board[4] == self.board[5] == symbol):
            print(text)
            return True
        elif len(list(filter(lambda x: type(x) is int, self.board))) == 0:
            print("НИЧЬЯ")
            return True
        else:
            return False

    def game_continue(self) -> bool:
        enter: str = input("Продолжить y/n? -> ")
        if enter.lower() == "y":
            self.__init__()
            return True
        else:
            exit()


if __name__ == '__main__':
    game_board = GameBoard()
    end_game = True
    while end_game:
        game_board.view()
        try:
            player = game_board.check_input()
            game_board.__set__("X", player)
            if game_board.is_win('X', "ВЫ ВЫИГРАЛИ"):
                game_board.game_continue()
            both = game_board.both()
            game_board.__set__("O", both)
            if game_board.is_win('O', "ВЫИГРАЛ БОТ"):
                game_board.game_continue()
        except KeyboardInterrupt:
            print("выход")
            exit()
