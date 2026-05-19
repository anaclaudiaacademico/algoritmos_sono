# sleep_algorithms
The experiments were conducted using 3 algorithms.

**Sparse with sleep** — the model is created by removing a percentage of the weights (epsilon) between layers, and between each training phase another fraction of the least significant weights is removed while new weights are randomly added.

**Sparse without sleep** — the model is created by removing a percentage of the weights (epsilon) between layers, but no weights are removed or added between training phases.

**Dense** — a dense network without weight removal/addition between training phases.


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
