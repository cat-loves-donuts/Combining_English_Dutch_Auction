# Combining_English_Dutch_Auction
Using English auctin first and then based on the number of rounds change the stratage to Dutch

First before the first, this code does not use any kind of package for message exchange. The code will read a list which is dounle of the number of the bidders. There are various of information of this auction like Auction ID, Auctioneer ID, Good name, Initial price and everything.

I wrote 3 files:
The first one is called Auctioneer which have the definition of the auctioneer agent. 
To create a auctioneer agent, the user needs to enter 11 different inputs and most of those inputs are good information. 
And I also defined 5 functions which the auction will be used during the auction. 
The function recive_Msg is using to receive the messages comes from bidders. 
The function start_auction is using to inform bidders that the auction is begin. 
The function call_for_proposal is using to inform bidders to give responds about the last message of auctioneer. 
The function English_process_Msg and Dutch_process_Msg are main function of English auction and Dutch auction, respectively.

The second one is called Bidder which have definition of bidders’ function and define. 
The user needs to enter 2 input, bidder ID and the percentage of increase the price, to create the Bidder. 
There are just two functions, the receive_Msg is for receiving messages from auctioneer and the process_Msg is dealing with the price and giving responds of the price.

The last one is the auction.py. 
In this file, I created a loop to keep doing the auction after user defined the bidder agents and auctioneer agents. 
In the loop, the tick is keep adding itself and if the winner appears the code will force to break the loop.
