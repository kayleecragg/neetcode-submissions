class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(image, r, c, og_colour):
            ROWS, COLS = len(image), len(image[0])

            # invalid fail
            if min(r, c) < 0 or r == ROWS or c == COLS or image[r][c] != og_colour:
                return
            # paint the tile the colour
            image[r][c] = color

            dfs(image, r + 1, c, og_colour)
            dfs(image, r  - 1, c, og_colour)
            dfs(image, r, c + 1, og_colour)
            dfs(image, r, c - 1, og_colour)


        r, c = sr, sc
        og_colour = image[sr][sc]
        if og_colour != color:
            dfs(image, r, c, og_colour)
        return image
