import scripts.main.datas.map_datas as map_datas
def check(tile, num):
    row = tile[1]
    column = tile[0]
    block = list()
    block.append(column // 3)
    block.append(row // 3)
    for y in range(len(map_datas.all_tiles)):
        for x in range(len(map_datas.all_tiles[y])):
            target_tile = (x,y)
            if not tile == target_tile:
                if column == target_tile[0]:
                    if num == map_datas.all_tiles[x][y]:
                        return False
                if row == target_tile[1]:
                    if num == map_datas.all_tiles[x][y]:
                        return False
                if block == [target_tile[0] // 3, target_tile[1] //3]:
                    if num == map_datas.all_tiles[x][y]:
                        return False
    return True






