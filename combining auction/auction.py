from Bidder import Bidder
from Auctioneer import Auctioneer

Message_from_auctioneer = []
Message_from_bidder = []

amount = 5
tick = 0
time = 20

Auctioneer0 = Auctioneer("call_for_proposal", 0,0,0,"Ticket:Aberdeen to London",50,time,amount,0.04,0.6,3)
Bidder0 = Bidder(0,0.1)
Bidder1 = Bidder(1,0.3)
Bidder2 = Bidder(2,0.5)
Bidder3 = Bidder(3,0.4)
Bidder4 = Bidder(4,0.9)

Auctioneer0.start_auction(tick)
for i in range(0,amount):
    Message_from_auctioneer.append(['call_for_proposal', 0, 0, i, 0, 'Ticket:Aberdeen to London', 27.0, 0, 0, 1])
    Message_from_bidder.append(['call_for_proposal', 0, 0, i, 0, 'Ticket:Aberdeen to London', 27.0, 0, 0, 1])

while(1):
    n = 0
    winner=[]
    for i in Message_from_auctioneer:
        if len(i) != 0:
            n = n + i[9]
    for i in Message_from_bidder:
        if len(i) != 0:
            n = n + i[9]
    if n == 0:
        print("break")
        break
    tick = tick + 1
    Bidder0.receive_Msg(Message_from_auctioneer[0])
    Bidder1.receive_Msg(Message_from_auctioneer[1])
    Bidder2.receive_Msg(Message_from_auctioneer[2])
    Bidder3.receive_Msg(Message_from_auctioneer[3])
    Bidder4.receive_Msg(Message_from_auctioneer[4])
    Bidder0.process_Msg()
    Bidder1.process_Msg()
    Bidder2.process_Msg()
    Bidder3.process_Msg()
    Bidder4.process_Msg()
    Message_from_bidder[0] = Bidder0.send_Msg
    Message_from_bidder[1] = Bidder1.send_Msg
    Message_from_bidder[2] = Bidder2.send_Msg
    Message_from_bidder[3] = Bidder3.send_Msg
    Message_from_bidder[4] = Bidder4.send_Msg
    winner = Auctioneer0.winner
    Auctioneer0.recive_Msg(Message_from_bidder,winner)
    winner = []

    if tick < (time-11):
        Auctioneer0.English_process_Msg(tick)
        Message_from_auctioneer = Auctioneer0.new_Msg
        Bidder0.receive_Msg(Message_from_auctioneer[0])
        Bidder1.receive_Msg(Message_from_auctioneer[1])
        Bidder2.receive_Msg(Message_from_auctioneer[2])
        Bidder3.receive_Msg(Message_from_auctioneer[3])
        Bidder4.receive_Msg(Message_from_auctioneer[4])
        Bidder0.process_Msg()
        Bidder1.process_Msg()
        Bidder2.process_Msg()
        Bidder3.process_Msg()
        Bidder4.process_Msg()
        Message_from_bidder[0] = Bidder0.send_Msg
        Message_from_bidder[1] = Bidder1.send_Msg
        Message_from_bidder[2] = Bidder2.send_Msg
        Message_from_bidder[3] = Bidder3.send_Msg
        Message_from_bidder[4] = Bidder4.send_Msg
        Auctioneer0.call_for_proposal(tick)
        Message_from_auctioneer = Auctioneer0.new_Msg
    if tick == (time - 11):
        Auctioneer0.English_process_Msg(tick)
        Message_from_auctioneer = Auctioneer0.new_Msg
        Bidder0.receive_Msg(Message_from_auctioneer[0])
        Bidder1.receive_Msg(Message_from_auctioneer[1])
        Bidder2.receive_Msg(Message_from_auctioneer[2])
        Bidder3.receive_Msg(Message_from_auctioneer[3])
        Bidder4.receive_Msg(Message_from_auctioneer[4])
        Bidder0.process_Msg()
        Bidder1.process_Msg()
        Bidder2.process_Msg()
        Bidder3.process_Msg()
        Bidder4.process_Msg()
        Message_from_bidder[0] = Bidder0.send_Msg
        Message_from_bidder[1] = Bidder1.send_Msg
        Message_from_bidder[2] = Bidder2.send_Msg
        Message_from_bidder[3] = Bidder3.send_Msg
        Message_from_bidder[4] = Bidder4.send_Msg
        Auctioneer0.call_for_proposal(tick)
        Message_from_auctioneer = Auctioneer0.new_Msg
    if (tick > (time - 11)) & (tick < time):
        Auctioneer0.Dutch_process_Msg(tick)
        Message_from_auctioneer = Auctioneer0.new_Msg
    if tick == time:
        Auctioneer0.Dutch_process_Msg(tick)
        Message_from_auctioneer = Auctioneer0.new_Msg

