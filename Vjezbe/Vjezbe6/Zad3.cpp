#include <iostream>
#include <list>
#include <vector>
#include <algorithm> 

void zamjena(int polje[], int i1, int i2){
    int c;
    c = polje[i2];
    polje[i2] = polje[i1];
    polje[i1] = c;
}

int main() {
    int polje[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int a, b;
    std::cout << "Upisite a i b: ";
    std::cin >> a >> b;
    std::cout << "Elementi izmedu a i b su: ";
    for (int i = a; i < b; i++) {
        std::cout << polje[i] << " ";
    }
    std::cout << "\n";

    std::sort(std::begin(polje), std::end(polje)); 
    std::reverse(std::begin(polje), std::end(polje));
    zamjena(polje, 0, 9);

    std::cout << "Nakon sortiranja, obrtanja redoslijeda i zamjena dva clana polje je jednako: ";

    for (int i = 0; i < 10; i++) {
        std::cout << polje[i] << " ";
    }
}