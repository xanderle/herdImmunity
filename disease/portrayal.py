def portrayCell(cell):
    '''
    This function is registered with the visualization server to be called
    each tick to indicate how to draw the cell in its current state.
    :param cell:  the cell in the simulation
    :return: the portrayal dictionary.
    '''
    assert cell is not None
    if cell.isAlive:
        color = "green"
    elif cell.isVaccinated:
        color = "blue"
    elif cell.isInfected:
        color = "red"
    elif cell.isImmune:
        color = 'yellow'
    return {
        "Shape": "rect",
        "w": 1,
        "h": 1,
        "Filled": "true",
        "Layer": 0,
        "x": cell.x,
        "y": cell.y,
        "Color": color
    }
