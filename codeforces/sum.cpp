#include <iostream>

int main()
{
    int n;
    std::cin >> n;

    int a, b, c;

    for (int i = 0; i < n; ++i)
    {
        std::cin >> a;
        std::cin >> b;
        std::cin >> c;

        if (std::abs(a - b) == c || a + b == c)
        {
            std::cout << "Yes"
                      << "\n";
        }
        else
        {
            std::cout << "No"
                      << "\n";
        }
    }

    return 0;
}
