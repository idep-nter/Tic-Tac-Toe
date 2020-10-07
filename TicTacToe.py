def main():
    """
    Main function prints an intro of the game at the start and creates and
    prints an empty table after that.
    In the while loop players are making moves, switching and using constantly
    updated table until any of winning or tie conditions are met.
    """
    intro()
    table = makeTable()
    printTable(table)
    while True:
        player = 'o'
        move = playerMove(table, char=player)
        table = makeTable(move, char=player, pTable=table)
        printTable(table)
        if checkIfOver(table, char=player):
            print('Congratulation, the player o WON!')
            break
        if checkIfTie(table):
            print('It\'s a tie!')
            break

        player = 'x'
        move = playerMove(table, char=player)
        table = makeTable(move, char=player, pTable=table)
        printTable(table)
        if checkIfOver(table, char=player):
            print('Congratulation, the player x WON!')
            break
        if checkIfTie(table):
            print('It\'s a tie!')
            break

def intro():
    print("""
=================================
GAME RULES:
Each Player can place one mark (or stone) per turn on the 3x3 grid.
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row
Let's start the game!
=================================
    """)

def makeTable(move=None, char=None, pTable=None):
    """
    It loads the previous table if it exists or creates one as a dictionary if not.
    If there is a move as an argument it sets a player's mark to a
    given position in the dictionary and returns the current table.
    """
    if pTable:
        table = pTable
    else:
        table = {1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : '', 8 : '',
                 9 : ''}
    if move:
        table[move] = char
    return table

def printTable(table):
    """
    Prints the formatted table.
    """
    line = '-'*12
    print(line)
    print(f'{table[1]:^3}|{table[2]:^3}|{table[3]:^3}')
    print(line)
    print(f'{table[4]:^3}|{table[5]:^3}|{table[6]:^3}')
    print(line)
    print(f'{table[7]:^3}|{table[8]:^3}|{table[9]:^3}')
    print(line)

def checkIfOver(table, char=None):
    """
    Returns True if any of conditions for winning is met.
    """
    if table[1] == char and table[2] == char and table[3] == char or \
        table[4] == char and table[5] == char and table[6] == char or \
        table[7] == char and table[8] == char and table[9] == char or \
        table[1] == char and table[4] == char and table[7] == char or \
        table[2] == char and table[5] == char and table[8] == char or \
        table[3] == char and table[6] == char and table[9] == char or \
        table[1] == char and table[5] == char and table[9] == char or \
        table[3] == char and table[5] == char and table[7] == char:
        return True

    return False


def checkIfTie(table):
    """
    Iterates through the table's values and returns True if there is no blank
    space on the table.
    """
    for value in table.values():
        if value == '':
            return False

    return True


def playerMove(table, char=None):
    """
    Asks player for a move and returns it after it checks if it's a single
    digit and if position on the table is available.
    """
    print('='*20)
    while True:
        move = int(input(f'Player {char} | Please enter your move number:'))
        if not move in list(range(1, 10)):
            print('...')
            continue
        if table[move] != '':
            print('You can\'t move there!')
            continue
        break
    print('=' * 20)
    print('=' * 20)

    return move

main()
