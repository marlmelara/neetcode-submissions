class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # indegree[i] = number of prerequisites required for course i
        indegree = [0] * numCourses 

        # adj[i] = list of courses that depend on course i
        adj = [[] for _ in range(numCourses)]


        # Create indegree and adj list
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
        
        # courses that can be taken
        queue = deque()

        # Add all the courses that have no prereqs in queue to be taken
        for i in range(numCourses):
            if indegree[i] ==0:
                queue.append(i)
        

        courseTaken = 0

        while queue:
            course = queue.popleft()
            courseTaken+=1

            for nextCourse in adj[course]:
                indegree[nextCourse] -= 1  # One prerequisite has been satisfied
                
                if indegree[nextCourse] == 0: 
                    # All prerequisites for nextCourse have now been satisfied
                    queue.append(nextCourse)
        

        return courseTaken == numCourses