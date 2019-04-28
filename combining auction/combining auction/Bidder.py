#!/usr/bin/env python
#coding:utf8

import random

class Bidder():
    def __init__(self,Bidder_ID, Increase):
        self.got_Msg_auctioneer = []
        self.current_auction = []
        self.send_Msg = []
        self.Increase = Increase
        self.Bidder_ID = Bidder_ID
        self.Budget = random.randint(100,250)
        print("Bidder",self.Bidder_ID," : has Budget",self.Budget,".")
        self.Highest_price = (self.Budget) * 0.9

    def receive_Msg(self,Msg_auctioneer):
        if len(Msg_auctioneer) != 0:
            self.got_Msg_auctioneer = Msg_auctioneer
            self.send_Msg = Msg_auctioneer
            self.current_auction = [Msg_auctioneer[1], Msg_auctioneer[2], Msg_auctioneer[4], Msg_auctioneer[5]]

    def process_Msg(self):
        if self.got_Msg_auctioneer[0] == "call_for_proposal":
            if self.current_auction != [self.got_Msg_auctioneer[1], self.got_Msg_auctioneer[2], self.got_Msg_auctioneer[4], self.got_Msg_auctioneer[5]]:
                print("Bidder", self.Bidder_ID, " : not understand.", "")
            elif self.got_Msg_auctioneer[3] != self.Bidder_ID:
                print("Bidder", self.Bidder_ID," : Sorry, you gave the offer to worry people.")
            else:
                if self.got_Msg_auctioneer[6] <= self.Budget:
                    if (self.got_Msg_auctioneer[6] * (1 + self.Increase)) <= self.Budget:
                        Bid_price = self.got_Msg_auctioneer[6] * (1 + self.Increase)
                    else:
                        Bid_price = self.Budget
                    tick = self.got_Msg_auctioneer[8] + 1
                    self.send_Msg[7] = Bid_price
                    self.send_Msg[8] = tick
                    self.send_Msg[0] = "proposal"
                    print("Bidder", self.Bidder_ID, "willing to pay ", Bid_price, "")
                else:
                    self.send_Msg = []
                    print("Bidder", self.Bidder_ID, "cannot offer the price and out.")
        if self.got_Msg_auctioneer[0] == "call_for_attitude":
            if self.current_auction != [self.got_Msg_auctioneer[1], self.got_Msg_auctioneer[2], self.got_Msg_auctioneer[4], self.got_Msg_auctioneer[5]]:
                print("Bidder", self.Bidder_ID, " : not understand.")
            elif self.got_Msg_auctioneer[3] != self.Bidder_ID:
                print("Bidder", self.Bidder_ID," : Sorry, you gave the offer to worry people.")
            else:
                if self.got_Msg_auctioneer[6] <= self.Budget:
                    tick = self.got_Msg_auctioneer[8] + 1
                    self.got_Msg_auctioneer[8] = tick
                    self.got_Msg_auctioneer[0] = "accept"
                    print("Bidder ", self.Bidder_ID, " accept this price and want to pay.")
                else:
                    self.send_Msg = []
                    print("Bidder", self.Bidder_ID, " cannot offer and sitting there.")
        if self.got_Msg_auctioneer[0] == "reject":
            if self.got_Msg_auctioneer[3] != self.Bidder_ID:
                print("Bidder", self.Bidder_ID," : Sorry, you gave the offer to worry people.")
            else:
                print("Bidder", self.Bidder_ID, "get the reject information")
        if self.got_Msg_auctioneer[0] == "accept":
            if self.got_Msg_auctioneer[3] != self.Bidder_ID:
                print("Bidder", self.Bidder_ID," : Sorry, you gave the offer to worry people.")
            else:
                print("Bidder", self.Bidder_ID, "get the accept information")
        if self.got_Msg_auctioneer[0] == "winner":
            self.send_Msg[9] = 0
            if self.got_Msg_auctioneer[3] == self.Bidder_ID:
                print("Bidder", self.Bidder_ID," : Ya hoo!!!!")
            else:
                print("Bidder", self.Bidder_ID," : Congratulation Bidder",self.got_Msg_auctioneer[3],"")
        if self.got_Msg_auctioneer[0] == "abortive_auction":
            self.send_Msg[9] = 0
            print("What a pitty.")



