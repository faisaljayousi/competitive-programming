#include <iostream>

int main()
{
    int n;
    std::cin >> n;

    int i = 1;
    int blocks = 1;

    while (n - blocks >= 0)
    {
        n = n - blocks;
        i++;
        blocks = i * (i + 1) / 2;
    }

    std::cout << i - 1 << "\n";
    return 0;
}