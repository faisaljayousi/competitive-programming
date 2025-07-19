#!/bin/bash

echo "🔧 Formatting C++ files..."
find . -type f \( -name "*.cpp" -o -name "*.h" \) -exec clang-format -i {} +

echo "🐍 Formatting Python files..."
find . -type f -name "*.py" -exec black {} +

echo "Formatting complete."
