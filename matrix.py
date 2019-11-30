class LedMatrix(object):
    def __init__(self):
        self.array = []
        self.jump = 16
        self.altnum = (1,3,5,7,9,11,13,15)

        self.start = 248
        for y in range(0,8):
            row = []
            for x in range(self.start+y, -1, -1*(self.jump) ):
                row.append(x)
                row.append(x - self.altnum[y])
            self.array.append(row)
    def ledarray(self):
        return self.array
