#include <iostream>
#include <fstream>
#include <string>
#include <map>



int challenge_one(std::string opponent, std::string chad){

    return 0;
}


int challenge_two(std::string opponent, std::string chad){
    
    if (opponent == "A") {
        return 0; 
    } else if (opponent == "B"){
        return 0;
    } else if (opponent == "C"){
        return 0;
    }

    
    return 0;
}


int main(){

    std::ifstream Hands("input.txt");
    std::string input;

    std::map<std::string, std::map<std::string, int>> big_map{ 
        {"ROUND_POINTS", {{"WIN_Points", 6}, {"DRAW_Points", 3}, {"LOOSE_Points", 0}}},
        {"ROUND_HAND_WIN",  {{"A",2 }, {"B", 3}, {"C", 1}}},
        {"ROUND_HAND_LOOSE", {{"A", 3}, {"B", 1}, {"C", 2}}}, 
        {"ROUND_HAND_DRAW", {{"A", 1}, {"B", 2}, {"C", 3}}}
    };

    int SCORE_1 = 0;
    int SCORE_2 = 0; 

    while (getline (Hands, input)){
        std::cout << input[0] << input[2] << std::endl; 
        challenge_two(std::string input[0], std::string input[2]);

    }

    return 0; 
}