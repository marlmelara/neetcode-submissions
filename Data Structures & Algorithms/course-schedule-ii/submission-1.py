class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # indegree and adj list
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # build a queue where we start with courses that have no pre req
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        # keep a running tally
        completedCourses = 0
        validCourses = []

        while queue:
            course = queue.popleft()
            validCourses.append(course) # append current course order
            completedCourses += 1

            for nextCourse in adj[course]:
                indegree[nextCourse] -= 1
                # check if the nextCourse we decremented is good to take
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        if completedCourses == numCourses:
            return validCourses

        else:
            return []