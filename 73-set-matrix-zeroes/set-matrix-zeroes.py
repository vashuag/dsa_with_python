class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col = 1
        for i in range(0,m):
            for j in range(0,n):
                if (matrix[i][j]==0):
                    matrix[i][0] = 0
                    if( j !=0):
                        
                        matrix[0][j] = 0
                    else:
                        col = 0
        
        for i in range(1,m):
            for j in range(1, n):
                if matrix[i][j] !=0:
                    if matrix[i][0] ==0 or matrix[0][j] ==0:
                        matrix[i][j] = 0


        if matrix[0][0] ==0:
            for j in range (0,n):
                matrix[0][j] = 0
        if col == 0:
            for i in range(0,m):
                matrix[i][0] = 0
        # m = len(matrix)
        # n = len(matrix[0])
        # # a = 0
        # # answer = [0] * m*n
        # # while (a<m):
        # #     for i in range(0,n):
        # #         if(matrix[a][i] == 0):
        # #             answer.insert(a+i,1)
        # #     a+=1  
        # # print(answer)

        # # for i in range(len(answer)-1):
        # #     if(answer[i]!=0):
        # #         print(answer[i])
        # #         k=0
        # #         while k<(max(m,n)):
        # #             print(answer[i])
        # #             matrix[k][i] = 0
        # #             matrix[i][k] = 0
        # #             k+=1

        # zero_rows= set()
        # zero_cols = set()
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             zero_rows.add(i)
        #             zero_cols.add(j)

        # for i in zero_rows:
        #     for j in range(n):
        #         matrix[i][j] = 0
        # for i in range(m):
        #     for j in zero_cols:
        #         matrix[i][j] = 0


                 
                    



        
            

        
                    


        