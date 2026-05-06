#include <iostream>
#include <string>
#include <map>

class Solution {
public:
    int romanToInt(std::string s) {
        int total = 0;
        char letter;
        int str_length = s.length();
        std::map<char, int> values = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        for (int i = 0; i < str_length; i++) {
            letter = s[i];
            if (i < str_length-1 && values[s[i]] < values[s[i+1]]) {
                total += values[s[i+1]] - values[s[i]];
                i++;
            } else {
                total += values[s[i]];
            }
        } 
        return total;
    }
};

int main() {
	Solution ret;
    std::string test_set[] = {"III", "IX", "LVIII", "MCMXCIV"};
    for (std::string test : test_set) {
        std::cout << ret.romanToInt(test) << '\n';
    }
}