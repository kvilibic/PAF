#include <iostream>

// Koristim Cramerovo pravilo, sustav jednadzbi se gleda kao matrica. Pomoću determinanti pronalazim x i y
// [a1 b1] [x] __ [c1]
// [a2 b2] [y] ‾‾ [c2]

int main(){
    float a1, b1, c1, a2, b2, c2, x, y;
    std::cout << "Upisite koeficijente (a1, b1, c1, a2, b2, c2): ";
    std::cin >> a1 >> b1 >> c1 >> a2 >> b2 >> c2;

    if (a1*b2 - b1*a2 == 0){
        std::cout << "Nema rjesenja.";
    }else{
        x = (c1*b2 - b1*c2)/(a1*b2 - b1*a2);
        y = (a1*c2 - c1*a2)/(a1*b2 - b1*a2);
        std::cout << "x = " << x << ", y = " << y;
    }
}