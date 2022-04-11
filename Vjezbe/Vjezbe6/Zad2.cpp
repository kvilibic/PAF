#include <iostream>

void funkcija(float x, float y, float s1, float s2, float r) {
    float a, b;
    a = abs(s1 - x);
    b = abs(s2 - y);

    if (a*a + b*b <= r*r) {
        std::cout << "Tocka se nalazi unutar kruznice" << std::endl;
    }else {
        std::cout << "Tocka se nalazi izvan kruznice" << std::endl;
    }
}

int main() {

    funkcija(5, 5, 3, 3, 3);

}