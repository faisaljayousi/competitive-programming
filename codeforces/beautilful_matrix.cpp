#include <iostream>

int main()
{
    int matrix[5][5];

    for (int i = 0; i < 5; ++i)
        for (int j = 0; j < 5; ++j)
            std::cin >> matrix[i][j];

    for (int i = 0; i < 5; ++i)
        for (int j = 0; j < 5; ++j)
            if (matrix[i][j] != 0)
            {
                std::cout << std::abs(i - 2) + std::abs(j - 2) << "\n";
                return 0;
            }

    return 0;
}
