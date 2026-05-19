# sleep_algorithms
The experiments were conducted using 3 algorithms.The model architecture is a modified version of the Sparse Evolutionary Training Multilayer Perceptron (SET-MLP)[Mocanu et al. 2018], in https://github.com/dcmocanu/sparse-evolutionary-artificial-neural-networks 

**Sparse with sleep** — the model is created by removing a percentage of the weights (epsilon) between layers, and between each training phase another fraction of the least significant weights is removed while new weights are randomly added (C).

<img width="708" height="270" alt="image" src="https://github.com/user-attachments/assets/2c3f5808-e94b-4b5e-b26e-72ec4eea4f71" />


**Sparse without sleep** — the model is created by removing a percentage of the weights (epsilon) between layers, but no weights are removed or added between training phases (B).

<img width="349" height="217" alt="image" src="https://github.com/user-attachments/assets/6fb44c54-62e9-4ed1-bd02-d16a72306d72" />


**Dense** — a dense network without weight removal/addition between training phases (A).

<img align="center" width="370" height="217" alt="image" src="https://github.com/user-attachments/assets/45a5f6ad-eaed-418b-a891-cbccdf7ec047" />



The “dense” and “sparse without sleep” networks share identical code, and their results are stored in the same files. The difference is that the dense network has sparsity (epsilon) equal to zero.

### Graphs
This section contains the code used to generate the graphs for analyzing the results.


### Results
The results files have .out extension and are formatted as CSV files. The experiments were divided into the following datasets: MNIST[0-4], MNIST[0-9], Fashion-MNIST, CIFAR-10, and CIFAR-100.

Cada arquivo .out possui os campos:

Each .out file contains the following fields:

**experiment** — describes whether the experiment is sparse with sleep or sparse without sleep.

**alpha** — number of neurons in the central layer of the model. It is important to note that the exact number of neurons in the intermediate layers depends on the dataset. For MNIST datasets, the total number of neurons in the intermediate layers is alpha × 3; for CIFAR datasets, it is alpha × 9. Example: if in the MNIST[0-4] dataset alpha = 4, the model will have 12 neurons in the intermediate layers. If the experiment was performed with alpha = 4 on CIFAR-10, it will have 36 neurons in the intermediate layers.

**epsilon** — percentage of weights removed between intermediate layers.

**sparse** — this value was initially created for model validation during the experiments, but became unnecessary later and is now set to null in the models.

**accuracy** — final model accuracy after 1000 epochs.

**seed**— seed value used in the experiment.

**dataset** — dataset used in the experiment.

**weights** — total number of weights used in the experiment.

### Utils
Section contains Python and shell scripts used for data processing, both for proper formatting before training on the supercomputer and for processing the experiment results.

References:
Mocanu, D. C., Mocanu, E., Stone, P., Nguyen, P. H., Gibescu, M., & Liotta, A. (2018). Scalable
training of artificial neural networks with adaptive sparse connectivity inspired by network
science, Nature Communications, 9, 2383-2394, https://doi.org/10.1038/s41467-018-04316-3
[Acessado em 04 de Outubro de 2019].
