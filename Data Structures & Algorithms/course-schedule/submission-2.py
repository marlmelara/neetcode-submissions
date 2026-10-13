class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # do Kahns algo so need adj and indegree
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course) # courses tied to prereq
            indegree[course] += 1 # keeps track of course prereq count needed

        queue = deque()
        # I want to initialize all courses that have no pre reqs
        for course in range(len(indegree)):
            if indegree[course] == 0:
                queue.append(course)

        completedCourses = 0

        while queue:
            course = queue.popleft()
            completedCourses += 1

            for nextCourse in adj[course]:
                indegree[nextCourse] -= 1
                # check if after taking pre req, can we take nextCourse
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        if completedCourses == numCourses:
            return True
        else:
            return False