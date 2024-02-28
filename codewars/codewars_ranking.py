class User:
    def __init__(self):
        self.ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank_index = 0
        self.rank = self.ranks[self.rank_index]
        self.progress = 0

    def inc_progress(self, question_rank):
        question_index = self.ranks.index(question_rank)
        if self.rank == 8:
            return None
        if self.rank_index == question_index:
            self.progress += 3
        elif self.rank_index - question_index == 1:
            self.progress += 1
        elif self.rank_index - question_index >= 2:
            pass
        else:
            self.progress += 10 * ((self.rank_index - question_index) ** 2)
        while self.progress >= 100:
            try:
                self.rank_index += 1
                self.rank = self.ranks[self.rank_index]
                self.progress = self.progress - 100
                if self.rank == 8:
                    self.progress = 0
            except IndexError:
                self.rank_index = 15
                self.rank = self.ranks[self.rank_index]
                self.progress = 0
