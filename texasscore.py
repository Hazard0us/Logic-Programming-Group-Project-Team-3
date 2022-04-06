
# **************************
# Scoring each player's hand
# Functions for each rule
# Scores are relative
# **************************

def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))

# AKQJ10 of same suit
def royalflush(cards):
  suit = cards[0][1]
  nonsuit = 0
  nonroyal = 0
  for x in cards:
    if (x[1]!=suit): 
      nonsuit = nonsuit+1
    if (x[0]!="Ace" and x[0]!="King" and x[0]!="Queen" and x[0]!="Jack" and x[0]!="10"):
      nonroyal = nonroyal+1
  if (nonsuit <= 2 and nonroyal <=2):
    return 200;
  else:
    return 0;

# Consecutive Cards of Same Suit
def straightflush(cards):
  suit = cards[0][1]
  l = []
  for x in cards:
    if (x[1]!=suit):
      return 0;
    if (x[0]=="Ace"):
      x[0]="14"
    if (x[0]=="King"):
      x[0]="13"
    if (x[0]=="Queen"):
      x[0]="12"
    if (x[0]=="Jack"):
      x[0]="11"
    l.append(int(x[0]))
  iscosec = checkConsecutive(l)
  if (iscosec):
    return 180;
  else:
    return 0;

# Four Cards of the same value
# Add the card value to the score to settle winner 
def fourofakind(cards):
  max = 0
  card = 0
  values = []
  for z in cards:
    values.append(z[0])
  for x in cards:
    cnt = values.count(x[0])
    if (cnt > max):
      max = cnt
      if (x[0]=="Ace"):
        x[0]="14"
      if (x[0]=="King"):
        x[0]="13"
      if (x[0]=="Queen"):
        x[0]="12"
      if (x[0]=="Jack"):
        x[0]="11"
      card = int(x[0])
  if (max == 4):
    return 160+card
  else:
    return 0;

# Three of a kind and two of a kind
def fullhouse(cards):
  values = []
  for z in cards:
    values.append(z[0])
  for x in cards:
    hastwo = 0
    hasthree = 0
    cnt = values.count(x[0])
    if (cnt == 2):
      hastwo = 1
    if (cnt == 3):
      hasthree = 1
  if (hastwo == 1 and hasthree==1):
    return 140
  else:
    return 0

# Same suite, any cards
def flush(cards):
  suit = cards[0][1]
  for x in cards:
    if (x[1]!=suit): 
      return 0
  return 120;

# Consecutive Cards, any suit
def straight(cards):
  l = []
  for x in cards:
    if (x[0]=="Ace"):
      x[0]="14"
    if (x[0]=="King"):
      x[0]="13"
    if (x[0]=="Queen"):
      x[0]="12"
    if (x[0]=="Jack"):
      x[0]="11"
    l.append(int(x[0]))
  iscosec = checkConsecutive(l)
  if (iscosec):
    return 100;
  else:
    return 0;

# Three of a kind
def threeofakind(cards):
  max = 0
  card = 0
  values = []
  for z in cards:
    values.append(z[0])
  for x in cards:
    cnt = values.count(x[0])
    if (cnt > max):
      max = cnt
      if (x[0]=="Ace"):
        x[0]="14"
      if (x[0]=="King"):
        x[0]="13"
      if (x[0]=="Queen"):
        x[0]="12"
      if (x[0]=="Jack"):
        x[0]="11"
      card = int(x[0])
  if (max == 3):
    return 80+card
  else:
    return 0;

# Two Pairs
def twopairs(cards):
  matches = 0
  values = []
  for z in cards:
    values.append(z[0])
  for x in cards:
    cnt = values.count(x[0])
    if (cnt == 2):
      matches = matches + 1
  if (matches == 4):
    return 60
  else:
    return 0;

# One Pair
def onepair(cards):
  max = 0
  card = 0
  values = []
  for z in cards:
    values.append(z[0])
  for x in cards:
    cnt = values.count(x[0])
    if (cnt > max):
      max = cnt
      if (x[0]=="Ace"):
        x[0]="14"
      if (x[0]=="King"):
        x[0]="13"
      if (x[0]=="Queen"):
        x[0]="12"
      if (x[0]=="Jack"):
        x[0]="11"
      card = int(x[0])
  if (max == 2):
    return 40+card
  else:
    return 0;

# High Card
def highcard(cards):
  card = 0
  for x in cards:
    if (x[0]=="Ace"):
      x[0]="14"
    if (x[0]=="King"):
      x[0]="13"
    if (x[0]=="Queen"):
      x[0]="12"
    if (x[0]=="Jack"):
      x[0]="11"
    if (int(x[0])>card):
      card = int(x[0])
  return card

# **********************
# Main Scoring Algorithm
# **********************
def score(suits,flop1,flop2,flop3,flop4,flop5,hcards,folds):
  scores = [] 
  print("")
  print("*** Scoring ***")
  for x in range(0,len(hcards)):
     folded = 0
     for f in folds:
       if ((x+1)==f):
         folded = 1
     if (folded==1):
     # print("Player",x+1,"folded")
       scores.append(0);
       continue
     # print("************")
     # print("Player",x+1)
     # print(hcards[x][1],"of",hcards[x][0])
     # print(hcards[x][3],"of",hcards[x][2])
     # print(flop1[1],"of",suits[flop1[0]])
     # print(flop2[1],"of",suits[flop2[0]])
     # print(flop3[1],"of",suits[flop3[0]])
     # print(flop4[1],"of",suits[flop4[0]])
     # print(flop5[1],"of",suits[flop5[0]])

     # Cards in format value, suit
     cards = []
     card1 = [hcards[x][1],hcards[x][0]]
     card2 = [hcards[x][3],hcards[x][2]]
     card3 = [flop1[1],suits[flop1[0]]]
     card4 = [flop2[1],suits[flop2[0]]]
     card5 = [flop3[1],suits[flop3[0]]]
     card6 = [flop4[1],suits[flop4[0]]]
     card7 = [flop5[1],suits[flop5[0]]]
     cards.append(card1)
     cards.append(card2)
     cards.append(card3)
     cards.append(card4)
     cards.append(card5)
     cards.append(card6)
     cards.append(card7)
     score = 0
     rf = royalflush(cards)
     sf = straightflush(cards)
     fa = fourofakind(cards)
     fh = fullhouse(cards)
     fl = flush(cards)
     st = straight(cards)
     ta = threeofakind(cards)
     tp = twopairs(cards)
     op = onepair(cards)
     hc = highcard(cards)
     if (rf>score):
       score = rf;
     if (sf>score):
       score = sf;
     if (fa>score):
       score = fa;
     if (fh>score):
       score = fh;
     if (fl>score):
       score = fl;
     if (st>score):
       score = st;
     if (ta>score):
       score = ta;
     if (tp>score):
       score = tp;
     if (op>score):
       score = op;
     if (hc>score):
       score = hc;
     scores.append(score)
  # print (scores)
  return scores
