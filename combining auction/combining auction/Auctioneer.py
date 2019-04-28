#!/usr/bin/env python
#coding:utf8

import random

class Auctioneer():
    def __init__(self, Msg_type, Auction_ID,Auctioneer_ID, Good_ID, Good_name, Reserve, time, amount_of_bidders,Increase,Decrease,Dutch_Increase):
        self.Auctioneer_ID = Auctioneer_ID
        self.Msg_type = Msg_type
        self.Auction_ID = Auction_ID
        self.Good_ID = Good_ID
        self.Good_name = Good_name
        self.got_Msg_Bidder = []
        self.accept = []
        self.new_Msg = []
        self.Increase = Increase
        self.Decrease = Decrease
        self.Dutch_Increase = Dutch_Increase
        self.Reserve = Reserve
        self.Initialprice = Reserve * (1 + self.Increase)
        self.time = time
        self.offer = 0
        self.number = amount_of_bidders
        self.winner = []

    def recive_Msg(self, Msg_bidder, winner):
        self.got_Msg_Bidder = []
        self.new_Msg = []
        self.winner = []
        for i in range(0, self.number):
            self.got_Msg_Bidder.append(Msg_bidder[i])
            self.new_Msg.append(Msg_bidder[i])
        self.winner = winner

    def start_auction(self, tick):
        print("Auctioneer", self.Auctioneer_ID," : Welcome everyone. I am auctioneer", self.Auctioneer_ID, ", the ID of this auction is: ", self.Auction_ID, ". Our ticket ID is:", self.Good_ID, " and the initial price is:",self.Initialprice, ". Let us start the auction.")
        self.new_Msg = []
        print("Auctioneer", self.Auctioneer_ID," : Please give me your price of the good.")
        for i in range(0, self.number):
            self.new_Msg.append(["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1])

    def call_for_proposal(self, tick):
        m = 0
        for i in self.new_Msg:
            if len(i) != 0:
                if i [0] == "winner":
                    m = m + 1
        if m == self.number:
            pass
        else:
            if tick < (self.time - 11):
                self.Initialprice = self.Initialprice * (1 + self.Increase)
                if self.offer > self.Initialprice:
                    self.Initialprice = self.offer
                print("Auctioneer", self.Auctioneer_ID," : The auction price right now is:", self.Initialprice,". Please give me your price of the good.")
                for i in range(0, self.number):
                    if len(self.got_Msg_Bidder[i]) != 0:
                        self.new_Msg[i][0] = "call_for_proposal"
                        self.new_Msg[i][6] = self.Initialprice
                        self.new_Msg[i][7] = self.offer
                        self.new_Msg[i][8] = tick
            if tick == (self.time-11):
                self.Initialprice = self.Initialprice * (1 + self.Increase)
                if self.offer > self.Initialprice:
                    self.Initialprice = self.offer
                self.Initialprice = self.Initialprice * self.Dutch_Increase
                if self.Initialprice < self.Reserve:
                    self.Initialprice = self.Reserve * self.Dutch_Increase
                print("_______________________Because of the time limitation, we have to change the auction into Dutch auction.______________________________")
                print("Auctioneer", self.Auctioneer_ID, " : The auction price right now is:", self.Initialprice,". Please give me your attitudes of the good price.")
                for i in range(0, self.number):
                    self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                    self.new_Msg[i][0] = "call_for_attitude"
                    self.new_Msg[i][6] = self.Initialprice
                    self.new_Msg[i][7] = self.Initialprice
                    self.new_Msg[i][8] = tick

    def English_process_Msg(self, tick):
        count = 0
        offer = 0
        accepter = 0
        bidder = []
        bid = []
        final = 0
        for i in self.got_Msg_Bidder:
            count = count + len(i)
        if count == 0:
            if len(self.winner) == 1:
                for i in range(0,self.number):
                    if len(self.got_Msg_Bidder[i]) != 0:
                        self.new_Msg[i][9] = 0
                if self.winner[0][7] >= self.Reserve:
                    print("Auctioneer", self.Auctioneer_ID," : Congratulations, Bidder ", self.winner[0][3], ", you winn this good in price ", self.winner[0][7])
                    bidder = int(self.winner[0][3])
                    for i in range(0,self.number):
                        self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                        self.new_Msg[i][0] = "winner"
                        self.new_Msg[i][3] = bidder
                else:
                    print("Auctioneer", self.Auctioneer_ID," : So sorry, this good is abortived by the price ", self.Initialprice)
                    for i in range(0,self.number):
                        if len(self.got_Msg_Bidder[i]) != 0:
                            self.new_Msg[i][0] = "abortive_auction"
            elif len(self.winner) > 1:
                for i in range(0,self.number):
                    self.new_Msg[i][9] = 0
                bidder = random.randint(0,(len(self.winner)-1))
                if self.winner[0][7] >= self.Reserve:
                    print("Auctioneer", self.Auctioneer_ID, " : We have a higher price now, it is ", self.winner[0][3])
                else:
                    print("Auctioneer", self.Auctioneer_ID, " : So sorry, this good is abortived by the price ",self.Initialprice)
                    for i in range(0,self.number):
                        if len(self.got_Msg_Bidder[i]) != 0:
                            self.new_Msg[i][0] = "abortive_auction"
            else:
                print("Auctioneer", self.Auctioneer_ID, " : So sorry, this good is abortived by the price ",self.Initialprice)
                for i in range(0,self.number):
                    if len(self.got_Msg_Bidder[i]) != 0:
                        self.new_Msg[i][9] = 0
                for i in range(0, self.number):
                    if len(self.got_Msg_Bidder[i]) != 0:
                        self.new_Msg[i][0] = "abortive_auction"
        else:
            self.winner = []
            for i in range(0, self.number):
                if len(self.got_Msg_Bidder[i]) != 0:
                    if self.got_Msg_Bidder[i][7] > offer:
                        offer = self.got_Msg_Bidder[i][7]
            for i in range(0, self.number):
                if len(self.got_Msg_Bidder[i]) != 0:
                    if (self.got_Msg_Bidder[i][7] == offer):
                        bid.append(self.got_Msg_Bidder[i][7])
                        bidder.append(self.got_Msg_Bidder[i][3])
                        self.winner.append(self.got_Msg_Bidder[i])
            accepter = self.winner[0][3]
            self.offer = offer
            for i in range(0,self.number):
                if len(self.new_Msg[i]) != 0:
                    if self.new_Msg[i][3] == accepter:
                        self.new_Msg[i][0] = "accept"
                        self.new_Msg[i][8] = tick-1
                    if self.new_Msg[i][3] != accepter:
                        self.new_Msg[i][0] = "reject"
                        self.new_Msg[i][8] = tick - 1

    def Dutch_process_Msg(self,tick):
        count = 0
        self.accept = []
        for i in range(0, self.number):
            if len(self.new_Msg[i]) != 0:
                if self.got_Msg_Bidder[i][0] == "accept":
                    self.accept.append(self.got_Msg_Bidder[i])
        if (tick > (self.time-11)) & (tick < self.time):
            if len(self.accept) == 1:
                for i in range(0, self.number):
                    if len(self.new_Msg[i]) != 0:
                        self.new_Msg[i][9] = 0
                if self.accept[0][6] >= self.Reserve:
                    print("Auctioneer", self.Auctioneer_ID," : Congratulations, Bidder ", self.accept[0][3], ", you winn this good in price ", self.accept[0][6])
                    for i in range(0, self.number):
                        self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                        self.new_Msg[i][0] = "winner"
                        self.new_Msg[i][3] = self.accept[0][3]
                        self.new_Msg[i][6] = self.accept[0][6]
                        self.new_Msg[i][7] = self.accept[0][6]
                        self.new_Msg[i][9] = 0
                else:
                    print("Auctioneer", self.Auctioneer_ID, " : So sorry, this good is abortived by the price ",self.accept[0][6])
                    for i in range(0, self.number):
                        self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                        self.new_Msg[i][0] = "abortive_auction"
                        self.new_Msg[i][9] = 0
            if len(self.accept) > 1:
                self.Initialprice = (self.Initialprice / self.Decrease - 10)
                print("Auctioneer", self.Auctioneer_ID, " : Looks like still some people intreasted in this good, our new price is ", self.Initialprice,", please give me your attitudes.")
                for i in range(0, self.number):
                    self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                    self.new_Msg[i][0] = "call_for_attitude"
                    self.new_Msg[i][6] = self.Initialprice
                    self.new_Msg[i][8] = tick + 1
            if len(self.accept) == 0:
                self.Initialprice = self.Initialprice * self.Decrease
                print("Auctioneer", self.Auctioneer_ID," : Ok, let's keep going, the new price is :", self.Initialprice)
                for i in range(0, self.number):
                    self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                    self.new_Msg[i][0] = "call_for_attitude"
                    self.new_Msg[i][6] = self.Initialprice
                    self.new_Msg[i][8] = tick + 1
        if tick == self.time:
            if len(self.accept) == 1:
                for i in range(0, self.number):
                    if len(self.new_Msg[i]) != 0:
                        self.new_Msg[i][9] = 0
                if self.accept[0][6] >= self.Reserve:
                    print("Auctioneer", self.Auctioneer_ID," : Congratulations, Bidder ", self.accept[0][3], ", you winn this good in price ", self.accept[0][6])
                    for i in range(0, self.number):
                        self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                        self.new_Msg[i][0] = "winner"
                        self.new_Msg[i][3] = self.accept[0][3]
                        self.new_Msg[i][6] = self.accept[0][6]
                        self.new_Msg[i][7] = self.accept[0][6]
                        self.new_Msg[i][9] = 0
                else:
                    print("Auctioneer", self.Auctioneer_ID, " : So sorry, this good is abortived by the price ",self.accept[0][6])
                    for i in range(0, self.number):
                        self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                        self.new_Msg[i][0] = "abortive_auction"
                        self.new_Msg[i][9] = 0
            if len(self.accept) > 1:
                for i in range(0, self.number):
                    if len(self.new_Msg[i]) != 0:
                        self.new_Msg[i][9] = 0
                count = random.randint(0,(len(self.accept))-1)
                if self.accept[count][6] > self.Reserve:
                    print("Auctioneer", self.Auctioneer_ID, " : Congratulations, Bidder ", self.accept[0][3],", you winn this good in price ", self.accept[0][6])
                    for i in range(0, self.number):
                        self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                        self.new_Msg[i][0] = "winner"
                        self.new_Msg[i][3] = self.accept[0][3]
                        self.new_Msg[i][6] = self.accept[0][6]
                        self.new_Msg[i][7] = self.accept[0][6]
                        self.new_Msg[i][9] = 0
                else:
                    print("Auctioneer", self.Auctioneer_ID, " : So sorry, this good is abortived by the price ",self.accept[0][6])
                    for i in range(0, self.number):
                        self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                        self.new_Msg[i][0] = "abortive_auction"
                        self.new_Msg[i][9] = 0
            if len(self.accept) == 0:
                print("Auctioneer", self.Auctioneer_ID, " : So sorry, this good is abortived by the price ",self.Initialprice)
                for i in range(0, self.number):
                    self.new_Msg[i] = ["call_for_proposal", self.Auction_ID, self.Auctioneer_ID, i, self.Good_ID, self.Good_name, self.Initialprice, 0, tick, 1]
                    self.new_Msg[i][0] = "abortive_auction"
                    self.new_Msg[i][9] = 0














