#include <iostream>

int main()
{
    int n, k;
    std::cin >> n >> k;

    for (int i = 0; i < k; ++i)
    {
        if (n % 10 == 0)
        {
            n = n / 10;
        }
        else
        {
            n -= 1;
        }
    }
    std::cout << n;
    return 0;
}
