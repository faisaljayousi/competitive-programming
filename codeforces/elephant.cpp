#include <iostream>

int main()
{
    int n;
    std::cin >> n;

    int steps[5] = {5, 4, 3, 2, 1};

    int counter = 0;
    int rem;

    for (auto step : steps)
    {
        rem = n / step;
        if (rem != 0)
        {
            n -= step * rem;
            counter += rem;
        }
    }

    std::cout << counter << "\n";
    return 0;
}
