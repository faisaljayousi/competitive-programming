#include <iostream>
#include <numeric>
#include <vector>

int main()
{
    int num_problems;
    std::cin >> num_problems;

    std::vector<int> nums(3);

    int counter = 0;

    for (int i = 0; i < num_problems; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            std::cin >> nums[j];
        }

        if (std::accumulate(nums.begin(), nums.end(), 0) > 1)
        {
            counter++;
        }
    }
    std::cout << counter << "\n";

    return 0;
}
