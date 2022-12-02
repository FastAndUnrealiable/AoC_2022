#include <iostream>
#include <fstream>
#include <string>
#include <map>

int main(){

    std::ifstream Hands("input.txt");
    std::string input;

    std::map<std::string, std::map<std::string, int>> big_map{ 
        {"ROUND_POINTS", {{"WIN_Points", 6}, {"DRAW_Points", 3}, {"LOOSE_Points", 0}}},
        {"ROUND_HAND_WIN",  {{"A",2 }, {"B", 3}, {"C", 1}}},
        {"ROUND_HAND_LOOSE", {{"A", 3}, {"B", 1}, {"C", 2}}}, 
        {"ROUND_HAND_DRAW", {{"A", 1}, {"B", 2}, {"C", 3}}}
    };


    while (getline (Hands, input)){

    }

    return 0; 
}