import random
import sys
sys.path.append('../graph')
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f'User {i}')

        #another possible way, to optimize
        target_friendships = numUsers * avgFriendships
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            userID = random.randint(1,self.lastID)
            friendID = random.randint(1,self.lastID)
            if self.addFriendship(userID,friendID):
                total_friendships += 2
            else:
                collisions += 1

        print(f"COLLISIONS: {collisions}")

        #one way, it is 0(n^2)
        # possible_friendships = []
        # # Create friendships
        # for UserID in self.users:
        #     for friendID in range(UserID+1, self.lastID+1):
        #         possible_friendships.append((UserID,friendID))

        # random.shuffle(possible_friendships)

        # for i in range(numUsers * avgFriendships // 2):
        #     friendship = possible_friendships[i]
        #     self.addFriendship(friendship[0],friendship[1])




        # my attempt, in progress
        # Create friendships
        # [i for i in range(0,9) if i not in [2,5,7]]
        # lister = []
        # for i in range(1,20):
        #     lista = [random.randint(0,10) for i in range(random.randint(0,4))]
        #     seta = set(lista)
        #     lister.append(seta)
        #     lista = []

        # print(lister)
        # random.shuffle(lister)
        # print(lister)

        # listy = [i for i in range(1,11)]
        # random.shuffle(listy)
        # for i in listy:
        #     self.addFriendship()

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue()
        queue.enqueue([userID])

        while queue.size() > 0:
            path = queue.dequeue()

            vertex = path[-1]

            if vertex not in visited:
                visited[vertex] = path

                for neighbor in self.friendships[vertex]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(f'friends: {sg.friendships}')
    # for i in sg.users:
    #     print(sg.users[i].name)

    connections = sg.getAllSocialPaths(1)
    print(f'connections: {connections}')

    total_social_pahts = 0
    for user_id in connections:
        total_social_pahts += len(connections[user_id])
    print(f"Avg length of social path: {total_social_pahts/len(connections)}")
