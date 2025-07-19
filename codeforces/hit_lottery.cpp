#include <array>
#include <iostream>

int main()
{
    int n;
    std::cin >> n;

    int count = 0;

    std::array<int, 5> bills = {100, 20, 10, 5, 1};

    for (auto v : bills)
    {
        while (n - v >= 0)
        {
            count++;
            n -= v;
        }
    }

    std::cout << count << "\n";

    return 0;
}