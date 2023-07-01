# def buidOrder(projects, dependencies):
#     projectGraph = buildGraph(projects, dependencies)
#     numProjects = len(projects)
#     order = [None] * numProjects

#     endIdx = 0
#     currentIdx = 0
#     while endIdx < numProjects:
#         endIdx = addNonDependants(projectGraph, order, endIdx)
#         currentProject = order[currentIdx]
#         currentIdx += 1

#         if currentProject == None:
#             return None

#         for dependantName in projectGraph.getProjectDependants(currentProject):
#             projectGraph.getProject(dependantName).decrementDependencies()

#     return order


# def buildGraph(projects, dependencies):
#     projectGraph = Graph()

#     for projectName in projects:
#         projectGraph.createProject(projectName)

#     for dependency in dependencies:
#         requiredProject = dependency[0]
#         dependantProject = dependency[1]
#         projectGraph.addEdge(requiredProject, dependantProject)

#     return projectGraph


# def addNonDependants(projectGraph, order, idx):
#     for project in projectGraph.getAllProjects():
#         if project.hasNoDependencies() and not project.hasBeenProcessed():
#             project.process()
#             order[idx] = project.getName()
#             idx += 1
#     return idx


# class Graph:
#     def __init__(self):
#         self.adjList = {}

#     def createProject(self, projectName):
#         self.adjList[projectName] = Project(projectName)

#     def addEdge(self, requiredProject, dependantProject):
#         self.adjList[requiredProject].addDependant(dependantProject)
#         self.adjList[dependantProject].incrementDependencies()

#     def getAllProjects(self):
#         return self.adjList.values()

#     def getProject(self, projectName):
#         return self.adjList[projectName]

#     def getProjectDependants(self, projectName):
#         return self.getProject(projectName).getDependants()


# class Project:
#     def __init__(self, projectName=None):
#         self.name = projectName
#         self.dependants = []
#         self.numDependencies = 0
#         self.isProcessed = False

#     def hasNoDependencies(self):
#         return self.numDependencies == 0

#     def incrementDependencies(self):
#         self.numDependencies += 1

#     def decrementDependencies(self):
#         self.numDependencies -= 1

#     def addDependant(self, project):
#         self.dependants.append(project)

#     def getDependants(self):
#         return self.dependants

#     def getName(self):
#         return self.name

#     def hasBeenProcessed(self):
#         return self.isProcessed

#     def process(self):
#         self.isProcessed = True


# --------------- Solution 2 -----------------
def buildOrder(projects, dependencies):
    projectGraph = buildGraph(projects, dependencies)
    order = []

    for project in projectGraph.getAllProjects():
        if not project.complete():
            if not dfs(project, projectGraph, order):
                return None
    return order


def buildGraph(projects, dependencies):
    graph = Graph()

    for projectName in projects:
        graph.createProject(projectName)

    for dependancy in dependencies:
        required = dependancy[0]
        dependant = dependancy[1]
        graph.addEdge(required, dependant)
    return graph


def dfs(project, projectGraph, order):
    if project.processing():
        return False

    project.markAsProcessing()
    for dependantName in project.getDependants():
        dependant = projectGraph.getProject(dependantName)
        if not dependant.complete():
            if not dfs(dependant, projectGraph, order):
                return False

    project.markAsComplete()
    order.insert(0, project.getName())
    return True


class Graph:
    def __init__(this):
        this.adjList = {}

    def createProject(self, projectName):
        self.adjList[projectName] = Project(projectName)

    def addEdge(self, requiredProject, dependantProject):
        self.adjList[requiredProject].addDependant(dependantProject)

    def getAllProjects(self):
        return self.adjList.values()

    def getProject(self, projectName):
        return self.adjList[projectName]

    def getProjectDependants(self, projectName):
        return self.getProject(projectName).getDependants()


class Project:
    def __init__(self, name=None):
        self.name = name
        self.dependants = []
        self.status = None

    def getName(self):
        return self.name

    def addDependant(this, dependant):
        this.dependants.append(dependant)

    def getDependants(this):
        return this.dependants

    def complete(this):
        return this.status == "Complete"

    def processing(this):
        return this.status == "Processing"

    def markAsComplete(this):
        this.status = "Complete"

    def markAsProcessing(this):
        this.status = "Processing"


projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [["a", "d"], ["f", "b"], ["b", "d"], ["f", "a"], ["d", "c"]]
print(buildOrder(projects, dependencies))
