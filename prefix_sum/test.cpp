#include <vector>
#include <iostream>
#include <set>

int main(void)
{
    std::vector<int> v = {1, 2, 3};

    std::cout << "앞? " << *v.begin() << "\n";
    std::cout << "뒤? " << *(v.end() - 1) << "\n";

    std::multiset<int> ms;
    ms.insert(10);
    ms.insert(5);
    ms.insert(10);

    return 0;
}