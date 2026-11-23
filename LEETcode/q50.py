
def floodFill(image, sr, sc, color):
    oldColor = image[sr][sc]

    if oldColor == color:
        return image

    rows = len(image)
    cols = len(image[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if image[r][c] != oldColor:
            return

        image[r][c] = color

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)

    return image


image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

sr = 1
sc = 1
color = 2

print(floodFill(image, sr, sc, color))
