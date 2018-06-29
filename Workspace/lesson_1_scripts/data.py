a = [[1, 2, 3], [4, 5, 6]]
#print (a[0])
myEmptyList = []
myListWithStuff = ["thing", "stuff", 3, 6, 9]
#print (myListWithStuff[3])
grid = [['SFFF'],
        ['FHFH'],
        ['FFFH'],
        ['CFFG']]
for c in grid: #c is an individual item inside of the grid
    row = "" #the rows are determined by the placement of spaces. a new space marks/ends a row, leading to a new line
    for r in c: #r is the items inside c
        row = row + r #don't start row there -- start it r spaces over from the last row, which will group the items together
        print r


grid = [[1,2,3,4], [5,6], [7,8,9]] #range = all integers up to stated value, len = length of the item (grid has 3 items)
for i in range(len(grid)): #i is a variable now being assigned an index, showing position rather than value (e.g. [1, 2, 3, 4] has i of 0)
    for j in range(len(grid[i])): #j is a var now being assigned an index of items in item i of the grid
        # e.g. for above: if focused on i=0 (item [1, 2, 3, 4]), 1 has a j of 0 in that item with an i of 0
        print(grid[i][j]), #this calls for the item in position j of the item in position i inside the grid
        # the comma prevents the print from going to a new line, keeping i items together
    print(" ")  #this extra print of a space adds a space to the end of the old line and starts a new line
    # The second print helps divide the i items into new lines

        #these loops are nested so that we print all the j items of one i item before moving on to the next i item.
            # thus, it prints in numeric order
        #seems like Python has streamlined it so that it intuitively knows that items end in commas or spaces