class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list) # userID : [(timestamp, tweetID), etc]
        self.userFollowers = defaultdict(set) # userID : [userID, and followeesID in list]
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.userTweets[userId].append((self.timestamp, tweetId))
        
    # fetches at MOST 10 most recent tweet IDs in the user's news feed
    def getNewsFeed(self, userId: int) -> List[int]:
        # we can get a maxHeap of the most recent tweet Id's from all our 
        # followees and compare those, then we pop the most recent
        # then if the followee that we popped has another tweet we add to maxHeap
        # otherwise we leave it alone and keep doing the same thing 
        if userId not in self.userFollowers[userId]:
            self.userFollowers[userId].add(userId)

        followees = self.userFollowers[userId]
        maxHeap = []
        heapq.heapify_max(maxHeap)

        for followeeId in followees:
            tweets = self.userTweets[followeeId]
            index = len(tweets) - 1 # most recent tweet index

            if index >= 0:
                timestamp, tweetId = tweets[index]

                # initialize our maxHeap with most recent tweets from followees
                heapq.heappush_max(maxHeap, (timestamp, tweetId, followeeId, index - 1)) 
                # important to add followeeId, and (nextIndex = index - 1),
                #b/c that's how we get our next most recent tweet if index >= 0

        result = []

        while maxHeap and len(result) < 10:
            timestamp, tweetId, followeeId, nextIndex = heapq.heappop_max(maxHeap)
            result.append(tweetId)

            if nextIndex >= 0:
                timestamp, tweetId = self.userTweets[followeeId][nextIndex]
                heapq.heappush_max(maxHeap, (timestamp, tweetId, followeeId, nextIndex - 1))

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFollowers[followerId].discard(followeeId)