
def generateCombinations(n,k):
        result = []
        def backtrack(path,index):

            if len(path) == k :
                result.append(path.copy())
                return

            if len(path) > k:
                return

            for num in range(index,n+1):
                path.append(num)
                backtrack(path,num+1)
                path.pop()


        backtrack([],1)

        return result



if __name__ == '__main__':

    print(generateCombinations(4,3))

    # Time: O(C(n, k) × k)
    # Auxiliary Space: O(k)
    # Space including  result: O(C(n, k) × k)