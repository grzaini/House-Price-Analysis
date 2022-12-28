#!/usr/bin/python

# Richard Stroop
# Virginia Tech Department of Computer Engineering
# 4-28-2011

import sys

# Max_D is the desired Order of the Golomb ruler
Max_D = int(sys.argv[1])

# Max_Length is the upper bound of the SHIFT algorithm
Max_Length = int(sys.argv[2])

# Create a push and pop architecture using lists to mimic GE1
List = []
Dist = []
Length = []
tempLength = 0
tempDist = 0b0
tempList = 0b1
List.append(tempList)
Dist.append(tempDist)
Length.append(tempLength)

bestSolution = 0
D = 1
# When D makes it back to 0, the algorithm has backtracked every possible position and is done
while (D != 0):
  tempLength = Length.pop()
  tempLength = tempLength + 1
  Length.append(tempLength)

  # Constantly increase the length while checking, if it ever becomes larger than the upper bound, backtrack
  if(tempLength>Max_Length):
    D = D - 1
    # Discard all of the top data in order to backtrack
    List.pop()
    Dist.pop()
    Length.pop()
  else:

    tempList = List.pop()
    tempDist = Dist.pop()

    # If the distances and marks have at least one bit in common
    if(tempDist & tempList != 0b0):
      # Just shift LIST
      List.append(tempList<<1)
      Dist.append(tempDist)
    else:

      # The distances and marks have no bits in common!
      # DIST[n+1] becomes DIST[n] OR'd with LIST[n]
      # LIST[n+1] becomes LIST[n] shifted once and OR'd with 1
      # LIST[n] is shifted incase we need to backtrack to it later
      Dist.append(tempDist)
      Dist.append(tempDist|tempList)
      List.append(tempList<<1)
      List.append(tempList<<1 | 0b1)

      # If the created ruler has the number marks that we are looking for
      if(D==Max_D-1):

        # Output it only if it is the first one found
        if(bestSolution==0):
          bestSolution = tempList<<1 | 0b1

        # Or smaller and thus a more optimal solution
        if(List.pop()<bestSolution):
          bestSolution = tempList<<1 | 0b1
        Dist.pop()
      else:

    # If the created ruler is smaller than what we are looking for
    # Make it bigger and search for another mark that will fit on the end of the ruler without going past the upper bound of the length
        Length.append(tempLength)
        D = D + 1


# For outputting purposes, this function converts the binary string to numbers by having a counter increase as it shifts through all of the bits and outputting the value of the counter if the current bit is high and thus a mark on the ruler

counter=0
while(bestSolution!=0):
  if(bestSolution & 1):
    print(counter)
  bestSolution = bestSolution >> 1
  counter = counter + 1
