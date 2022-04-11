#include <iostream>

void funkcija(float x1, float y1, float x2, float y2) {
    float a, b;
    a = (y2-y1)/(x2-x1);
    b = y1 - a*x1;

    std::cout << "Jednadžba pravca je y = " << a << "x + " << b << std::endl;
}

int main() {
    funkcija(8, 8, 4, 6);
}


