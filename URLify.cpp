// CTCI 

#include <iostream>
#include <string>

std::string& urlify(std::string& str, int t_len) {
  int left = t_len - 1;
  int right = str.length() - 1;

  while (left < right) {
    if (str[left] == ' ') {
      str[right] = '0';
      str[right - 1] = '2';
      str[right - 2] = '%';
      right -= 3;
    } 
    else {
      str[right] = str[left];
      right -= 1;
    }
    left -= 1;
  }
  return str;
}

int main() {
  std::string s = "Mr John Smith    ";

  std::cout << urlify(s, 13);
}