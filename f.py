%reset -f
import pandas as pd 
import numpy as np
#%%
userRatingList = { "user1" : {"history" : [],"StarSum":0,"CompletedTasks" : 0,
                                       "Cancelledtasks" : 0 },
                    "user2" :  {"history" : [],"StarSum":0,"CompletedTasks" : 0,
                                       "Cancelledtasks" : 0 },
                    "user3" :  {"history" : [],"StarSum":0,"CompletedTasks" : 0,
                                       "Cancelledtasks" : 0 },
                   "user4" :  {"history" : [],"StarSum":0,"CompletedTasks" : 0,
                                       "Cancelledtasks" : 0 },
                   "user5" :  {"history" : [],"StarSum":0,"CompletedTasks" : 0,
                                       "Cancelledtasks" : 0 },
                   "user6" :  {"history" : [],"StarSum":0,"CompletedTasks" : 0,"Cancelledtasks" : 0 }}
                   
                   
userRatingList["user1"]                   
#%%
userRatingProbabilities =  { "user1" : { 0,0,1,2,2,3,3,4,4,4,5,5 },
                             "user2" : { 0,0,0,1,2,3,3,4,4,4,5,5 },
                             "user3" : { 0,1,1,2,2,2,3,3,3,4,4,5 },
                             "user4" : { 0,0,0,1,2,2,3,3,3,4,4,5 },
                             "user5" : { 0,1,2,3,3,4,4,4,4,5,5,5 },
                             "user6" : { 0,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30 }}
   
userRatingProbabilities["user6"]

#%%
def getScoreIncrement (starsum, completedTasks,cancelledTasks, newStarRating) :
		yes=1;
		if (newStarRating == 0):
			newCompleted = 0;
			newCancelledTasks = cancelledTasks + 1;
			cancelsFactor = 1;
			StarFactor = (newStarRating + (0.8*starsum))/(newCompleted + (0.8*completedTasks));
			
		else :
			newCompleted = 1;
			newCancelledTasks = cancelledTasks + 0;
			StarFactor = (newStarRating + (0.8*starsum))/(newCompleted + (0.8*completedTasks));
			
		if (completedTasks==0):
			return yes;
		else:
			cancelsFactor = 1 - ((newCancelledTasks/(newCancelledTasks+completedTasks))**2);
		return (cancelsFactor*StarFactor)


getScoreIncrement(0,0,0,4)

#%%
            
def getScoreDecrement(last5Cancels):
	if (last5Cancels == 0) :
		return(1.875);
	else :
		return(1.875-(0.375*last5Cancels/(6-last5Cancels)))

getScoreDecrement(4)


def getNewRating(userID, newTaskRating):
	userInfo = userRatingList["user6"]
	newUserHistory = [newTaskRating, userInfo['history']]
	if len(newUserHistory) >5:
		newUserHistory = newUserHistory[1:5]
	increment = getScoreIncrement (userInfo['StarSum'], userInfo['CompletedTasks'],userInfo['Cancelledtasks'],newTaskRating)
	decrement = getScoreDecrement(len(np.where(newUserHistory == 0 )))
	newRating = increment + decrement
	yes = 0;
	no =1;
	if (newTaskRating == 0 ):
		CompletedTasks = userInfo['CompletedTasks'] + yes;
		Cancelledtasks = userInfo['Cancelledtasks'] + no;
	else:
		CompletedTasks = userInfo['CompletedTasks'] + no;
		Cancelledtasks = userInfo['Cancelledtasks'] + yes;
	if ( userInfo['CompletedTasks'] < 4):
		Rating = 'NewUser';
	else :
		Rating = newRating;

	newUserInfo = {'history' : newUserHistory,
		         'StarSum': userInfo['StarSum'] + newTaskRating,
		          'CompletedTasks' : CompletedTasks,
		         'Cancelledtasks' : Cancelledtasks,
		          'Rating' : Rating}
	userRatingList[userID] = newUserInfo;
	return newRating

getNewRating("user6",5)
