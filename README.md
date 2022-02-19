## [WIP] Expressivity of Quantum model in terms of Fourier series.

### Completed
1. Entire Report 
1. Codebase for replication of every scenarios of the paper [1]. It works for the degree 1 Fourier Series
### TODO(s)

1. Write OOP style code to eliminate code repetition
1. Use custom 3 qubit system like the GHZ-state instead of  StronglyEntanglingLayers that authors have used in their git repo
1. Replicate the figure 3 from the paper
1. Replicate for degree 5 Fourier series
1. Separate the report and the codes into two python notebooks and two corresponsding pdf files

This repository provides an extensive and comprehensive study/review to the article [1]. Albeit, this work only covers the section I and section II, they are extensive nevertheless. I‘ve invested multiple hours and a meticulous efforts to simplify the loaded mathematical notions and symbols to make it more palatable to the reader. Since you are here, I presume you are looking to break in to the article. I hope my work will help you on your way.

The article is study about the effects of data encoding on the expressive power of variational quantum machine learning models. The encoding parameters like number of gates and scaling of the frequency in trainable model determines the expressivity. The underlying notion is the quantum model can be exchanged in terms of the Fourier series.

$$f_{\theta}(x) = \sum_{n\in\Omega} \, c_n(\theta)e^{in x}$$
$$f_{\theta}(x) \, = \,\, <0|U^\dagger (x,\theta) M U(x,\theta)|0>$$
$$  \sum_{n\in\Omega} \, c_n(\theta)e^{in x} =   \,\, <0|U^\dagger (x,\theta) M U(x,\theta)|0>$$

A prior knowledge of the Fourier analysis [2] is mandatory to learn from the article. Plus I would suggest the eigen-decomposition is a cool insights [3]. 

In the abstract section of the article the authors succinctly provide the objectives of their hard work.

>Here we investigate how the strategy with which data is encoded into the model inﬂuences the expressive power of parametrised quantum circuits as function approximators. We show that one can naturally write a quantum model as a partial Fourier series in the data, where the accessible frequencies are determined by the nature of the data encoding gates in the circuit. By repeating simple data encoding gates multiple times, quantum models can access increasingly rich frequency spectra. We show that there exist quantum models which can realise all possible sets of Fourier coeﬃcients, and therefore, if the accessible frequency spectrum is asymptotically rich enough, such models are universal function approximators.

### Folder Structure
1. The folder "reports" contains the pyhton notebook, and its html and pdf file format. The pdf file would be a great way to study my work.

1. The folder "results" contains the ouput from the code in the python notebook.

### Results
In work too I found the results 

### Closing note
If you find this repository helpful please consider to fork or star it. Thank you for your visit!
### References

[1] Schuld, Maria, Ryan Sweke, and Johannes Jakob Meyer. "Effect of data encoding on the expressive power of variational quantum-machine-learning models." Physical Review A 103.3 (2021): 032430.

[2] Weisstein, Eric W. "Fourier Series." From MathWorld--A Wolfram Web Resource. https://mathworld.wolfram.com/FourierSeries.html 

[3] Weisstein, Eric W. "Eigen Decomposition." From MathWorld--A Wolfram Web Resource. https://mathworld.wolfram.com/EigenDecomposition.html

[4] Schuld, M., Sweke, R. and Meyer, J., 2022. GitHub - XanaduAI/expressive_power_of_quantum_models. [online] GitHub. Available at: <https://github.com/XanaduAI/expressive_power_of_quantum_models> [Accessed 18 February 2022]