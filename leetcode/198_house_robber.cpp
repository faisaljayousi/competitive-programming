class Solution
{
public:
    int rob(vector<int>& nums)
    {
        const int n = nums.size();

        if (n == 1)
        {
            return nums[0];
        }

        if (n == 2)
        {
            return std::max(nums[0], nums[1]);
        }

        std::vector<int> arr(n);

        arr[0] = nums[0];
        arr[1] = std::max(nums[0], nums[1]);

        for (int j = 2; j < n; ++j)
        {
            arr[j] = std::max(nums[j] + arr[j - 2], arr[j - 1]);
        }

        return std::max(arr[n - 1], arr[n - 2]);
    }
};
