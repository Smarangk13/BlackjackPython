def showCards(cards):
    for card in cards:
        print(card,'\t', end='')
    print()

def cardTotal(cards):
    total = 0
    aces = 0
    for card in cards:
        val = card.split()[0]
        if val in ['K','Q','J']:
            total += 10

        elif val == 'A':
            aces += 1
            total += 11

        else:
            total += int(val)

    while aces > 0:
        if total <= 21:
            break
        total -= 10
        aces -= 1

    return total