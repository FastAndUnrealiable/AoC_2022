#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>


int main() {

    std::ifstream Calories("input.txt");
    std::string input;
    std::vector<int> cal_value_vector;

    int tmp_cal_sum = 0;

    while (getline (Calories, input))
    {
       
        if (input.empty())
        {
            cal_value_vector.push_back(tmp_cal_sum);
            tmp_cal_sum = 0;
        }
        else
        {
            tmp_cal_sum = tmp_cal_sum + stoi(input);
        }
    }

    Calories.close();

    std::sort(std::begin(cal_value_vector), std::end(cal_value_vector));

    for (int i = 1; i < 4; i++){
        std::cout << cal_value_vector[cal_value_vector.size()-i] << std::endl;
    }

    return 0;
}


