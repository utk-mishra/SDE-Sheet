def nextPermutation(self, nums: List[int]) -> None:
        # didn't have a clue - tuf optimized soln
        # find a break point -  from the back of arr, where arr[i] becomes less than arr[i+1]
        # if break point found - search element smaller than arr[i] in the right half and swap, then reverse the whole right half
        # if not found - reverse the whole array and return

        #[1,2,3] - main intuition -  all increasing permutations are slightly greater than the before one. Their values are also in ascending order
        # observation 1 - next perm. should have Longer prefix match - find a[i] > a[i+1]
        # observation 2 - find a no. > a[i] on the right but the smallest one, so that you can stay close
        # observation 3 - after swap, the left becomes slighly bigger than original one, now minimize the right part by reversing it since it is the largest it can be
        breakPointIndex = -1
        #1. Findbreak point
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                breakPointIndex = i
                break
        # return reverse if no bp (last Permutation case) 
        if breakPointIndex == -1:
            return nums.reverse()

        # 2. swap ith with least in the right side
        for i in range(len(nums) - 1, breakPointIndex, -1):
            if nums[breakPointIndex] < nums[i]:
                nums[breakPointIndex], nums[i] = nums[i], nums[breakPointIndex]
                break
        
        # 3. return with reversed right half
        nums[breakPointIndex + 1:] = reversed(nums[breakPointIndex + 1:])

        #time - O(n)
        #space - O(1)