class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> preproduct (nums.size());
        vector<int> postproduct (nums.size());
        int preP = 1, postP = 1;

        for (int i=0;i<nums.size()-1;i++){
            preP *= nums[i];
            preproduct[i] = preP;
        }

        for(int i=nums.size()-1;i>=0;i--){
            postP*=nums[i];
            postproduct[i] = postP;
        }
        
        vector<int> res;
        for(int i=0;i<=nums.size()-1;i++){
            if(i==0){
                //first element
                res.push_back(postproduct[i+1]);
            }
            else if(i==nums.size()-1){
                //last element
                res.push_back(preproduct[i-1]);
            }
            else{
                int prod = preproduct[i-1]*postproduct[i+1];
                res.push_back(prod);
            }
        }
        return res;
    }
};
