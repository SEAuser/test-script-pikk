import random

# bikin deck kartu standar
suits = ["♠ Spade", "♥ Heart", "♦ Diamond", "♣ Club"]
ranks = ["2", "3", "4", "5", "6", "7", "8",
         "9", "10", "J", "Q", "K", "A"]

deck = [f"{r} {s}" for s in suits for r in ranks]

# kocok kartunya
random.shuffle(deck)
print(f"Total kartu: {len(deck)}")

# bagiin ke 3 pemain, masing2 dapet 5 kartu
def deal(deck, players=3, cards_each=5):
    hands = {}
    for i in range(players):
        hands[f"Pemain {i+1}"] = deck[i*cards_each : (i+1)*cards_each]
    return hands

hasil = deal(deck)
for nama, kartu in hasil.items():
    print(f"{nama}: {', '.join(kartu)}")
