def buidOrder(projects, dependencies):
    projectGraph = buildGraph(projects, dependencies)
    numProjects = len(projects)
    order = [None] * numProjects

    endIdx = 0
    currentIdx = 0
    while endIdx < numProjects:
        endIdx = addNonDependants(projectGraph, order, endIdx)
        currentProject = order[currentIdx]
        currentIdx += 1

        if currentProject == None:
            return None

        for dependantName in projectGraph.getProjectDependants(currentProject):
            projectGraph.getProject(dependantName).decrementDependencies()

    return order


def buildGraph(projects, dependencies):
    projectGraph = Graph()

    for projectName in projects:
        projectGraph.createProject(projectName)

    for dependency in dependencies:
        requiredProject = dependency[0]
        dependantProject = dependency[1]
        projectGraph.addEdge(requiredProject, dependantProject)

    return projectGraph


def addNonDependants(projectGraph, order, idx):
    for project in projectGraph.getAllProjects():
        if project.hasNoDependencies() and not project.hasBeenProcessed():
            project.process()
            order[idx] = project.getName()
            idx += 1
    return idx


class Graph:
    def __init__(self):
        self.adjList = {}

    def createProject(self, projectName):
        self.adjList[projectName] = Project(projectName)

    def addEdge(self, requiredProject, dependantProject):
        self.adjList[requiredProject].addDependant(dependantProject)
        self.adjList[dependantProject].incrementDependencies()

    def getAllProjects(self):
        return self.adjList.values()

    def getProject(self, projectName):
        return self.adjList[projectName]

    def getProjectDependants(self, projectName):
        return self.getProject(projectName).getDependants()


class Project:
    def __init__(self, projectName=None):
        self.name = projectName
        self.dependants = []
        self.numDependencies = 0
        self.isProcessed = False

    def hasNoDependencies(self):
        return self.numDependencies == 0

    def incrementDependencies(self):
        self.numDependencies += 1

    def decrementDependencies(self):
        self.numDependencies -= 1

    def addDependant(self, project):
        self.dependants.append(project)

    def getDependants(self):
        return self.dependants

    def getName(self):
        return self.name

    def hasBeenProcessed(self):
        return self.isProcessed

    def process(self):
        self.isProcessed = True


projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [["a", "d"], ["f", "b"], ["b", "d"], ["f", "a"], ["d", "c"]]
print(buidOrder(projects, dependencies))
