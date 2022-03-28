import scripts.main.datas.map_datas as map_datas
def check(tile, num):
    row = tile[1]
    column = tile[0]
    print(f"row: {row}; column: {column}")
    for y in range(len(map_datas.all_tiles)):
        for x in range(len(map_datas.all_tiles[y])):



