#include <iostream>

int main()
{
    int w;
    std::cin >> w;

    if (w % 2 != 0 || w <= 3)
    {
        std::cout << "NO";
    }
    else
    {
        std::cout << "YES";
    }
}
