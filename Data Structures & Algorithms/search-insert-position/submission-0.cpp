class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1;
        bool found = false;
        while (left<=right){
            int mid = (left+right)/2;

            if (target < nums[mid]){
                right = mid-1;
            }
            else if (target>nums[mid]){
                left = mid+1;

            }
            else{
                found = true;
                return mid;
            }
        }
        if (found == false){
            return left;
        
        }
    }
};