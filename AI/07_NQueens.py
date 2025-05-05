class NQueensSolver:
    def __init__(self,n):
        self.N=n
        self.board=[-1]*n
        self.cols=[False]*n
        self.diag1=[False]*(2*n-1)
        self.diag2=[False]*(2*n-1)
        self.solution_count=0

    def solve(self):
        self.place_queen(0)
        if self.solution_count==0:
            print(f"No solution exists for N= {self.N}")

    def place_queen(self, row):
        if row== self.N:
            self.solution_count+=1
            self.print_board()
            return
        
        for col in range(self.N):
            if not self.cols[col] and not self.diag1[row - col + self.N - 1] and not self.diag2[row + col]:
                self.board[row] = col
                self.cols[col] = self.diag1[row - col + self.N - 1] = self.diag2[row + col] = True

                self.place_queen(row + 1)

                self.cols[col] = self.diag1[row - col + self.N - 1] = self.diag2[row + col] = False
                self.board[row] = -1
    
    def print_board(self):
        print(f"\nSolution {self.solution_count}:")
        for i in range(self.N):
            row=["Q" if self.board[i]==j else "." for j in range(self.N)]
            print(" ".join(row))

n=int(input("Enter Value of N(number of queens ): "))
solver=NQueensSolver(n)
solver.solve()