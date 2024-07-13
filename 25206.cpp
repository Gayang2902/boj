#include <iostream>
#include <map>

std::map<std::string, double> table = {
    {"A+", 4.5},
    {"A0", 4.0},
    {"B+", 3.5},
    {"B0", 3.0},
    {"C+", 2.5},
    {"C0", 2.0},
    {"D+", 1.5},
    {"D0", 1.0}
};

int main(void)
{
    std::string name, mark;
    double credit = 0.0;

    double total_credit = 0.0;
    double grade = 0.0;

    for (int i = 0; i < 20; i++) {
        std::cin >> name >> credit >> mark;
        if (!mark.compare("P")) continue;
        
        total_credit += credit;
        if (!mark.compare("F")) continue;
        grade += credit * table[mark];
    }
    
    std::cout << grade / total_credit << std::endl;

    return 0;
}