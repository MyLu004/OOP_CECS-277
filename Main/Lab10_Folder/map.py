#Map : read from the map txt



class Map:
    """
    Singleton - the map
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if not Map._initialized:
            self._file = open("map.txt", "r")
            self._lines = self._file.readlines()
            ''' 
            Creating a map and the reveal map
            '''
            self._map = []
            self._revealed = []
            for line in self._lines:
                self._map2 = []
                self.reveal2 = []
                for item in line.strip():
                    self._map2.append(item)
                    self.reveal2.append(False)

                self._map.append(self._map2)
                self._revealed.append(self.reveal2)
            Map._initialized = True
            self._file.close()

    def __getitem__(self, row):
        return self._map[row]

    def __len__(self):
        return len(self._map)

    def show_map(self, loc): #print out the map for the player
        m = ''
        for i in range(len(self._map)):
            for j in range(len(self._map[0])):
                if i == loc[0] and j == loc[1]:
                    m += '*'
                elif self._revealed[i][j]: #if True
                    m += self._map[i][j]
                else:
                    m += 'x'
            m += '\n'
        return m

    def reveal(self, loc): #loc = [row,col]
        """sets the value in the 2D revealed list at the specified location to True"""
        self._revealed[loc[0]][loc[1]] = True
        #print(self._revealed[loc[0]][loc[1]])

    def remove_at_loc(self, loc):
        """overwrites the character in the map list at the specified location with an ‘n’"""
        self._map[loc[0]][loc[1]] = 'n'

