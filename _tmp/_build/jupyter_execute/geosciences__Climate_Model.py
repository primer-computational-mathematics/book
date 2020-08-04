#import relevant modules

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# Constructing an energy balance model 


The <b>energy flux density at the surface of the Earth</b> can be calculated from the inverse square law, given the power of the Sun $3.86$x$10^{26}W$ ($E_S$), and the distance between the Sun and the Earth $1.5$x$10^{11}m$ ($R$): 

$$S_o=\frac{E_S}{4\pi R^{2}}$$

This is the <b>solar constant $S_o$</b>, which is roughly 1365 $Wm^{-2}$.

Energy balance model is crucial in building a climate model, since atmospheric dynamics are driven by the input of energy into the climate system. 

Let's first make several <b>assumptions</b> about the Earth:
1. It is a perfect blackbody
2. Its albedo is 0.3, which is the average terrestrial albedo
3. It is in radiative equilibrium i.e. energy in = energy out
4. Equal solar irradiation on the surface of the Earth

Recall that albedo (α) is the <b>reflectance of an object over all wavelengths</b>, which measures how well a surface reflects EM radiation. 

We already know the energy flux density at the surface of the Earth = the solar constant $S_o$.

Thus, the energy flux density ($Wm^{-2}$) into the Earth is:

$$M_{in}=S_o(1-α)$$ 

In terms of total energy flux ($W$):

$$E_{in}=S_o\pi R_E^2(1-α)$$

where $R_E$ is the radius of the Earth.

The energy flux density emitted is described by Stefan-Boltzmann Law:

$$M_{out}=σ𝑇_K^{4}$$

where σ=<b>Stefan-Boltzmann constant</b>=$5.67$x$10^{-8}Wm^{-2}K^{-4}$, and $T_K$ is <b>absolute temperature</b>. 

In terms of total energy flux:

$$E_{out}=4\pi R_E^2σ𝑇_K^{4}$$

At <b>radiative equilibrium</b>, energy absorbed = energy emitted, thus:

$$E_{in}=E_{out}$$

$$S_o\pi R_E^2(1-α)=4\pi R_E^{2}σ𝑇_K^{4}$$

$$\frac{1}{4}S_o(1-α)=σ𝑇_K^{4}$$ 

Recall $σ𝑇_K^{4}=M_{out}$, thus $\frac{1}{4}S_o(1-α)=M_{in}$ at radiative equilibrium.

Rearranging for $T_K$:

$$T_K=(\frac{S_o(1-α)}{4σ})^{\frac{1}{4}}$$

Substituting albedo=0.3, temperature on the surface of the Earth is <b>-18˚C</b>.

# define a function to calculate temperature in degrees Celsius for a given albedo
# al = albedo, s = stefan-boltzmann constant, S_o = solar constant
def find_temp(al, S_o=1365, s=5.67e-8):
    return ((S_o*(1-al))/(4*s))**0.25-273

print("When albedo = %.1f, surface temperature on Earth would be %.d˚C." % (0.3, find_temp(0.3)))

But the average temperature on Earth should be around <b>14˚C</b>, so something in the model must be wrong.

Actually, some of the assumptions are not valid and are too simple.

#### Assumption 1 

The Earth is not a perfect blackbody, because it doesn't radiate perfectly.

#### Assumption 2 

Albedo = 0.3 is actually pretty accurate. As you'll see below, after accounting for the Earth being an imperfect blackbody, the surface temperature calculated is very sensible.

#### Assumption 3

Equilibrium is easily disturbed, especially by <b>positive feedbacks</b>.

#### Assumption 4 

The Earth is a sphere, so heat absorbtion (and heat emission) is not uniform.

## Emissivity

To improve the model and address assumption 1, <b>emissivity ε</b> is introduced to describe the <b>difference in the range of radiation emitted between the object and an ideal black body</b>.

Including this 'fudge factor', Stefan-Boltzmann Law becomes:

$$M_{out}=εσT_K^{4}$$

Since $M_{in}=M_{out}$,

$$\frac{1}{4}S_o(1-α)=εσT_K^{4}$$

$$T_K=(\frac{S_o(1-α)}{4εσ})^{\frac{1}{4}}$$

It is found that the emissivity of the Earth is 0.62, and substituting this into the equation gives 14˚C, proving that albedo=0.3 is a valid assumption.

# define a function to find the temperature with a given emissivity
# e = emissivity

def find_new_temp(al, S_o=1365, e=0.62, s=5.67e-8):
    return ((S_o*(1-al))/(4*e*s))**0.25-273

print("Including emissivity, with albedo of 0.3, temperature on Earth would be %.d˚C." % (find_new_temp(0.3)))

# make an array of values of albedo between 0 and 1
albedo = np.array([0.01*i for i in range(101)])

#calculate temperature with different albedo
new_temp = find_new_temp(albedo)

# plot figure
plt.figure(figsize=(8,6))
plt.plot(albedo, new_temp, 'b')
plt.plot(albedo[29], new_temp[29], 'ro', label='albedo=%.1f' % (albedo[29])) 
plt.xlabel('Albedo')
plt.ylabel('Temperature (Degrees Celsius)')
plt.title('A plot of temperature vs emissivity when emissivity=0.62', fontsize=14)
plt.legend(loc='best', fontsize=10)
plt.grid(True)
plt.show()

## Conclusion

This model is still very crude, since plenty of things are still not taken into account, such as greenhouse effect, clouds, position of continents, vegetation, positive and negative feedbacks, etc. 

In a real climate model, other factors also have to be included such as atmospheric dynamics, climate variability like ENSO, human influence, etc.

However, this example shows how scientists build climate models by using equations from physics, making approximations and assumptions, including parameters to account for any variability, and adjusting the values of parameters so that it resembles the real world when it is run.

For more information about how other factors are accounted for in a model, including greenhouse effect and positive feedbacks, you can visit the __[New York University Maths Department website](https://math.nyu.edu/faculty/kleeman/zero_dim_ebm.html)__.

### References

- Practical 1 of the Climate module