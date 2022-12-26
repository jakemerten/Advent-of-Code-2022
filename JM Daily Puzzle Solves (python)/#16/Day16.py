from collections import defaultdict
from collections import deque
from functools import cache
import itertools as it
import os

ValveList = []
with open("day16input.txt", "r") as data:
    for t in data:
        Line = t.strip().split()
        Name, Rate, Tunnels = Line[1], int(Line[4][5:-1]), tuple(Line[9:])
        NewTuple = (Name, Rate, Tunnels)
        ValveList.append(NewTuple)

NumberValves = len(ValveList)
ValveNameDict = defaultdict()
ValveIntDict = defaultdict()
for n, v in enumerate(ValveList):
    Name, Rate, Tunnels = v
    Tunnels = list(Tunnels)
    for m, t in enumerate(Tunnels):
        if len(t) > 2:
            Tunnels[m] = t[:-1]
    Tunnels = tuple(Tunnels)
    ValveNameDict[Name] = (n, Rate, Tunnels)
    ValveIntDict[n] = Rate
Psuedocache = set()

def ParseValve(Minutes, Location, ActiveValveInt, NumberValvesTotal, PastPressure):
    Index, Rate, Tunnels = ValveNameDict[Location]
    IndexBinary = bin(Index)[2:]
    ValveBinary = bin(ActiveValveInt)[2:]
    while len(IndexBinary) < 6:
        IndexBinary = "0" + IndexBinary
    while len(ValveBinary) < NumberValvesTotal:
        ValveBinary = "0" + ValveBinary
    NewBinary = IndexBinary + ValveBinary
    StateInt = int(NewBinary, 2)
    if StateInt in Psuedocache:
        return 0
    Psuedocache.add(StateInt)

    ActivePressure = 0
    for n, v in enumerate(ValveBinary):
        if v == "1":
            NewRate = ValveIntDict[n]
            ActivePressure += NewRate
    TotalPressure = ActivePressure + PastPressure

    if Minutes >= 30:
        return TotalPressure
    
    if Rate > 0 and ValveBinary[Index] == "0":
        NewActiveBinary = list(ValveBinary)
        NewActiveBinary[Index] = "1"
        NewActiveInt = int("".join(NewActiveBinary), 2)
        NewTuple = (Minutes+1, Location, NewActiveInt, TotalPressure)
        PathQueue.append(NewTuple)
    
    for t in Tunnels:
        NewTuple = (Minutes+1, t, ActiveValveInt, TotalPressure)
        PathQueue.append(NewTuple)
    
    return TotalPressure + (30-Minutes)*ActivePressure

PathQueue = deque()
PathQueue.append((1, "AA", 0, 0))
Cycles = 0
Part1Answer = 0
while PathQueue:
    Minutes, Location, ValveInt, CurrentPressure = PathQueue.popleft()
    NextEntry = ParseValve(Minutes, Location, ValveInt, NumberValves, CurrentPressure)
    if NextEntry > Part1Answer:
        Part1Answer = NextEntry
    Cycles += 1

##########Part 2

P2IntDict = defaultdict()
P2NameDict = defaultdict()
WorkingValveSet = set()
WorkingValveList = []
Index = 0
for v in ValveList:
    Name, Rate, Tunnels = v
    if Rate == 0:
        continue
    WorkingValveSet.add(Name)
    P2IntDict[Index] = Rate
    P2NameDict[Name] = (Index, Rate)
    WorkingValveList.append(Name)
    Index += 1


PathLengthDict = defaultdict()
def BFS(Valve):
    VisitedSet = set()
    VisitedSet.add(Valve)
    Queue = deque()
    Queue.append((0, Valve))
    while Queue:
        Length, Position = Queue.popleft()
        _, _, Tunnels = ValveNameDict[Position]
        if Position in WorkingValveSet and Length != 0:
            PathLengthDict[(Valve, Position)] = Length
        if Position == "AA":
            PathLengthDict[(Position, Valve)] = Length
        for t in Tunnels:
            if t in VisitedSet:
                continue
            Queue.append((Length+1, t))
            VisitedSet.add(t)

for v in WorkingValveSet:
    BFS(v)
StatesSeen = 0

@cache
def P2Parse(Minutes, Location, ArrivalTime, ActiveValveInt, PlayersRemaining):
    global StatesSeen

    if Minutes == 0 and PlayersRemaining == 1:
        return P2Parse(26, "AA", 0, ActiveValveInt, 0)
    if Minutes == 0 and PlayersRemaining == 0:
        return 0
    
    StatesSeen += 1
    if StatesSeen % 100000 == 4:
        print(StatesSeen)
    if ArrivalTime > 0:
        return P2Parse(Minutes-1, Location, ArrivalTime-1, ActiveValveInt, PlayersRemaining)
    
    ValveBinary = bin(ActiveValveInt)[2:]
    while len(ValveBinary) < len(WorkingValveSet):
        ValveBinary = "0" + ValveBinary
    Score = 0
    if Location != "AA":
        Index, Rate = P2NameDict[Location]
        Score = Minutes*Rate
        NewValveInt = list(ValveBinary)
        NewValveInt[Index] = "1"
        NewValveInt = int("".join(NewValveInt), 2)
    
    Scoring = [Score]
    
    for v in WorkingValveList:
        NewIndex, NewRate = P2NameDict[v]
        if v == Location:
            continue
        if ValveBinary[NewIndex] == "1":
            continue
        NewLength = PathLengthDict[Location, v]
        if NewLength > Minutes:
            continue
        if Location == "AA":
            NewScore = Score + P2Parse(Minutes-1, v, NewLength, ActiveValveInt, PlayersRemaining)
            Scoring.append(NewScore)
        else:
            NewScore = Score + P2Parse(Minutes-1, v, NewLength, NewValveInt, PlayersRemaining)
            Scoring.append(NewScore)
    
    if PlayersRemaining == 1 and Location != "AA":
        Scoring.append(Score + P2Parse(26, "AA", 0, NewValveInt, 0))
    return max(Scoring)


print(PathLengthDict)


Part2Answer = P2Parse(26, "AA", 0, 0, 1)

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")