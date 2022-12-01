#include <iostream>
#include <fstream>
#include <string>

std::string input;

int main() {

    std::ifstream Calories("input.txt");

    while (getline (Calories, input)){

        std::cout << input;
    }

    Calories.close();

}
