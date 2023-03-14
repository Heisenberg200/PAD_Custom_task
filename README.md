## PAD_Custom_task
# Author: Corman Daniel
# Review: Volosenco Maxim
 
  # Description: 
   
   The gateway having 2 endpoints( GET and POST) is receiving 
   the request that is containing the body with the data, and
   it parses the body spliting it into the rows. Next it snds
   the patsed set to the services from the list of services 
   using the Round Robin algorythm ( in order first to the 0
   servie then to the 1st service and so on...)
    The Services are creating the db connection and if the r
     and check if the request method is POST and store the a
      asterisks into the database sqlite as (id, name) where 
      name are the asterisks.
      After the gateway has finished with all the requests
      it connects to the database, and it takes the last n re
      gistry(where the n is the number od rows in the body of
      the request. And finaly it returns the result.
   
   
   
   
