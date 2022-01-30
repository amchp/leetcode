class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if(k % nums.size() == 0)return;
        if(k > nums.size())k = k % nums.size();
        int visited = 0;
        for(int i = 0; i < k; ++i){
            int p = (nums.size() - (k % nums.size()) + i);
            int n = i % nums.size();
            int tmp = nums[p];
            int tmp2 = nums[n];
            do{
                visited++;
                nums[n] = tmp;
                p = (p + k) % nums.size();
                n = (n + k) % nums.size();
                tmp = tmp2;
                tmp2 = nums[n];
                
            }while(p != nums.size() - (k % nums.size()) + i);
            if(visited == nums.size())return;
        }
    }
};