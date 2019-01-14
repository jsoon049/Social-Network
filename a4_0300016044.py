#Family name: Jeremy Soong
#Student number: 300016044
# Course: IT1 1120 
# Assignment Number 4

import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    
    i=0
    a=[]
    for friend in friends:
        if friend.isdigit()==False:
            friend=friend.split(" ")
            uId=int(friend[0])
            fId=int(friend[1])
            a.append((uId,fId))
            a.append((fId,uId))
    a=sorted(a)
    z=[]
    for i in range(len(a)):
        x=a[i][0]
        y=[a[i][1]]
        for j in range(i+1,len(a)):
            if a[j][0]==x:
                y.append(a[j][1])
        z.append((x,y))
    d=[]
    for item in z:
        if not item[0] in d:
            d.append(item[0])
            network.append(item)
    return network


def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    for user in network:
        if user1==user[0]:
            x=user
            break
    for user in network:
        if user2==user[0]:
            y=user
            break
    for item in x[1]:
        if item in y[1]:
            common.append(item)
    return common
   
    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''
    mcommon=0
    a=0
    for x in network:
        y=x[0]
        if user in x[1] or user==x[0]:
            continue
        else:
            if len(getCommonFriends(user,y,network))>mcommon:
                mcommon=len(getCommonFriends(user,x[0],network))
                a=x[0]
    if a>0:
        return a
    else:
        return None            


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    count=0
    for user in network:
        x=len(user[1])
        if x>=k:
            count=count+1
    return count


def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    max=0
    for user in network:
        if len(user[1])>max:
            max=len(user[1])
    return max
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    for user in network:
        if len(user[1])==maximum_num_friends(network):
            max_friends.append(network.index(user))
    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''
    total=0
    for user in network:
        total=total+len(user[1])
    avg=total/len(network)
    return avg
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    flag=False
    i=0
    x=len(network)
    while flag==False and i<len(network):
        if (len(network[i][1])+1)==x:
            flag=True
        i=i+1
    return flag


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    flag=False
    x=str(input("Enter an integer for a user ID: "))
    while flag==False:
        try:
            a=x
            x=indexes(int(x),network)
            network[int(x)]
            if int(x)<0:
                print("That user ID does not exist. Try again.")
                x=str(input("Enter an integer for a user ID: "))
                continue
            elif int(x)>=0 or int(x).strip()>=0:
                flag=True
        except IndexError:
            print("That user ID does not exist. Try again.")
            x=str(input("Enter an integer for a user ID: "))
        except ValueError:
            print('That was not an integer. Please try again.')
            x=str(input("Enter an integer for a user ID: "))
        else:
            flag=True
    a=int(a)
    return a

##helper function##
def indexes(x,lst):
    '''(int,2dlist)->int
    Return index of list that contains x in the 2dlist'''
    for user in lst:
        if x==user[0]:
            x=lst.index(user)
            break
    return int(x)

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")


