#include <iostream>

class Particle{
    private:
        double t, x, y, vx, vy;
        double dt;
        double a = -9.81;

        void move();
    
    public:
        Particle(double v0, double theta, double x0, double y0, double korak=0.000001);
        ~Particle();

        double range();
        double time();
};