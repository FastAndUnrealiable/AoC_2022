#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>


int main() {

    std::ifstream Calories("input.txt");
    std::string input;
    std::vector<int> CAL_VALUE_VECTOR;

    int TMP_CAL_SUM = 0;

    while (getline (Calories, input))
    {
       
        if (input.empty())
        {
            CAL_VALUE_VECTOR.push_back(TMP_CAL_SUM);
            TMP_CAL_SUM = 0;
        }
        else
        {
            TMP_CAL_SUM = TMP_CAL_SUM + stoi(input);
        }
    }

    Calories.close();

    std::sort(std::begin(CAL_VALUE_VECTOR), std::end(CAL_VALUE_VECTOR));

    for (int i = 1; i < 4; i++){
        std::cout << CAL_VALUE_VECTOR[CAL_VALUE_VECTOR.size()-i] << std::endl;
    }

    return 0;
}


