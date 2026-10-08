class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list) # userID : [(timestamp, tweetID), etc]
        self.userFollowers = defaultdict(set) # userID : [userID, and followeesID in list]
        self.timestamp = timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.userTweets[userId].append((self.timestamp, tweetId))
        
    # fetches at MOST 10 most recent tweet IDs in the user's news feed
    def getNewsFeed(self, userId: int) -> List[int]:
        # we do minHeap and our idea is to extend the list with all tweets 
        # from user and followees, then minHeap it and cut it until we are left
        # with the ten most recent tweet Ids then we 
        if userId not in self.userFollowers[userId]:
            self.userFollowers[userId].add(userId)
            
        minHeap = []
        result = []
        allFollowerIds = self.userFollowers[userId]
        for followeeId in allFollowerIds:
            minHeap.extend(self.userTweets[followeeId])

        if minHeap:
            heapq.heapify(minHeap)

        while len(minHeap) > 10:
            heapq.heappop(minHeap)

        # we then flip our minHeap to a maxHeap and pop until minHeap is empty
        maxHeap = minHeap
        heapq.heapify_max(maxHeap)

        while maxHeap:
            timestamp, tweetId = heapq.heappop_max(maxHeap)
            result.append(tweetId)

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowers[followerId].add(followeeId)
        # make sure to check if own Id in this list
        # because we will use this dict for getting feed,
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # first check if followerId is valid and has followeeId's
        if self.userFollowers[followerId] and followeeId in self.userFollowers[followerId]:
            self.userFollowers[followerId].remove(followeeId)