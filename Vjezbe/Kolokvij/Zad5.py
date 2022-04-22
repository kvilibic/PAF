import Projectile as pro
import matplotlib.pyplot as plt

p1 = pro.ProjectileDrop(2000, 200)

t, x, y = p1.meta(10000, 50)
print("Projektil ce pogoditi metu ako ga ispustimo nakon {:.2f} s.".format(t))


plt.plot(x, y)
plt.grid()
plt.show()

# Odlucio sam uzeti vjetar kao akceleraciju u x smjeru. 
# Pokusavao sam prvo da je vx konstantan i vx = vx + v_vjetar no to je nefizikalno - vjetar treba ubrzavat/usporavat projektil
# Drugo sam pokusavao googlati "drag force" gdje treba povrsina objekta i jos neke varijable, tragao sam za formulom, ali neuspjesno
# Na kraju iako ne skroz fizikalno, akceleracija u x smjeru mi izgleda kao najizglednije rjesenje

p2 = pro.ProjectileDrop(2000, 200)

t, x, y = p2.meta_vjetar(10000, 50, -10)
print("Projektil ce pogoditi metu ako ga ispustimo nakon {:.2f} s.".format(t))

plt.plot(x, y)
plt.grid()
plt.show()
