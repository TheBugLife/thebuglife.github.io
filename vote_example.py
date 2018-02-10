from steem import Steem

#######
# Example code for voting on a SPECIFIC POST
# With an already imported wallet / account
# Requiring user to input passphrase set at wallet import stage.
#########

steem = Steem()
permlink = '@dzyan/ice-climbing'

try:
   steem.vote(permlink,100)
   print ("Succesfully upvoted!")
except Exception as e:
   print (repr(e))
