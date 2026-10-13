class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(len(indegree)):
            if indegree[course] == 0:
                queue.append(course)

        completedCourses = 0
        validCourseOrder = []

        while queue:
            course = queue.popleft()
            completedCourses += 1
            validCourseOrder.append(course)

            for nextCourse in adj[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        if completedCourses == numCourses:
            return validCourseOrder
        else:
            return []