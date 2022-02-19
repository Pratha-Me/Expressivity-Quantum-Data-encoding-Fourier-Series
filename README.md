## Expressivity of Quantum model in terms of Fourier series.

This repository provides an extensive and comprehensive study/review to the article [1]. Albeit, this work only covers the section I and section II, they are extensive nevertheless. I‘ve invested numerous hours and a meticulous efforts to simplify the loaded mathematical notions and symbols to make it more palatable to the reader. Since you are here, I presume you are looking to break in to the article. I hope my work will help you on your way.

The article is study about the effects of data encoding on the expressive power of variational quantum machine learning models. The encoding parameters like number of gates determines the expressivity and can be exchanged in terms of the Fourier series. A prior knowledge of the Fourier analysis [2] is mandatory to learn from the article. Plus I would suggest the eigen-decomposition is a cool insights [3]. 

In the abstract section of the article the authors succinctly provide the objectives of their hard work.

>Here we investigate how the strategy with which data is encoded into the model inﬂuences the expressive power of parametrised quantum circuits as function approximators. We show that one can naturally write a quantum model as a partial Fourier series in the data, where the accessible frequencies are determined by the nature of the data encoding gates in the circuit. By repeating simple data encoding gates multiple times, quantum models can access increasingly rich frequency spectra. We show that there exist quantum models which can realise all possible sets of Fourier coeﬃcients, and therefore, if the accessible frequency spectrum is asymptotically rich enough, such models are universal function approximators.

### References

[1] Schuld, Maria, Ryan Sweke, and Johannes Jakob Meyer. "Effect of data encoding on the expressive power of variational quantum-machine-learning models." Physical Review A 103.3 (2021): 032430.

[2] Weisstein, Eric W. "Fourier Series." From MathWorld--A Wolfram Web Resource. https://mathworld.wolfram.com/FourierSeries.html 

[3] Weisstein, Eric W. "Eigen Decomposition." From MathWorld--A Wolfram Web Resource. https://mathworld.wolfram.com/EigenDecomposition.html

[4] Schuld, M., Sweke, R. and Meyer, J., 2022. GitHub - XanaduAI/expressive_power_of_quantum_models. [online] GitHub. Available at: <https://github.com/XanaduAI/expressive_power_of_quantum_models> [Accessed 18 February 2022]