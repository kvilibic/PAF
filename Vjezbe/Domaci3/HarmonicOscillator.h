#include <iostream>
#include <vector>

using namespace std;

class HarmonicOscillator{
    private:
        double x, v, a, k, m, t, dt;

        void move();
    
    public:

        HarmonicOscillator(double x0, double k, double m, double korak=0.01);
        ~HarmonicOscillator();

        vector<double> t_list, x_list, v_list, a_list;

        double gibanje();
};