import random

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.score = 0
        self.bust = False

    def hit_or_stand(self):
        # convert to try and except to catch errors
        while True:
            try:
                print("Hit (H) or Stand (S)")
                ans = input("H or S")
                if ans.upper() == "H":
                    return True
                elif ans.upper() == "S":
                    return False
                else:
                    raise Exception
                
            except Exception:
                print("I did not understand that")
    

    def display_hand(self,Ihand,score):
        return ("Player has:",Ihand,"with a score of",score)
    


class Dealer():
    def __init__(self):
        self.hand=[]
        self.score=0
        self.bust = False

class Deck():
    def __init__(self):
        self.suits = ['Hearts','Diamonds','Clubs','Spades']
        # jokers are not used in blackjack
        self.values = [2,3,4,5,6,7,8,9,10,'Q','K','A']
        self.cards = [] # list of tuples
        for Suit in self.suits:
            for Value in self.values:
                self.cards.append((Value,Suit)) 


    def shuffle(self):
        self.new = self.cards
        random.shuffle(self.new)
        self.cards=self.new
        return self.cards
        ## self.cards=random.shuffle(self.cards) does not work as the shuffle function returns None
     


class Gameplay():
    
    def __init__(self):
      self.p1=Player('Aaron')
      self.dealer=Dealer()
      self.deck=Deck()

    
    def setup_deal(self):
        self.deck.shuffle()
        for i in range(2):
            self.p1.hand.append(self.deck.cards.pop())
            self.dealer.hand.append(self.deck.cards.pop())
        print(f"{self.p1.name} has {self.p1.hand} and the dealer has {self.dealer.hand[0]} plus a hidden card")
        

    def deal_card(self, deal):
        deal.append(self.deck.cards.pop())


    def dealer_turn(self):
        while True:
            self.dealer.score=self.calculate(self.dealer.hand)
            print(self.dealer.hand)
            print("Dealer score =",self.dealer.score)
            print()
            if self.dealer.score > 17:
                break
            else:
                self.deal_card(self.dealer.hand)

        
    def calculate(self,hand):
        # needs to be updated to reduce the value of an ace to 1 if required 
        ace = False
        ace_num=0
        score = 0
        for i in hand:
            if i[0] == "A":
                ace = True
                ace_num +=1
                score+= 11
            elif i[0] == "Q" or i[0] == "K":
                score+=10
            else:
                score = score + i[0]
        while True:
            if score > 21 and ace_num >= 1:
                score = score -10 
                ace_num -= 1
            else:
                break

        return score
    
    
    def play(self):
        print("Starting game")
        self.setup_deal()
        while True:
            if self.p1.hit_or_stand() == True:
               self.deal_card(self.p1.hand)
               self.p1.score= self.calculate(self.p1.hand)
               print(self.p1.display_hand(self.p1.hand,self.p1.score))
               print()
            else:
                break
        self.dealer_turn()
        self.endGame()


    def endGame(self):
        self.p1.score= self.calculate(self.p1.hand)
        self.dealer.score=self.calculate(self.dealer.hand)
        print(self.p1.name,"Had a score of:",self.p1.score)
        print()
        print("The dealer had a score of:",self.dealer.score)
        print()
        """
        Work in progress
        
        if self.p1.score> 21:
            print(self.p1.name,"went bust with a score of",self.p1.score)
        else:
            if self.p1.score == 21:
                print(self.p1.name,"has blackjack")

        """
        


        

                       
def main():
    gameplay=Gameplay()
    gameplay.play()

if __name__=='__main__':
    main()