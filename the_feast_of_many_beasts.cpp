#include <string>
using namespace std;

bool feast(string beast,string dish){
  //get first character and get the last character of the dish
  char beast_first_char = beast[0];
  char beast_last_char = beast[beast.length() - 1];
  char dish_first_char = dish[0];
  char dish_last_char = dish[dish.length() - 1];
  
//   if(beast_first_char == dish_first_char && beast_last_char == dish_last_char)
// {
//     return true;
//   }
  return (beast_first_char == dish_first_char && beast_last_char == dish_last_char);
  }