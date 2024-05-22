# Random-Radon-Transformation

Repository consists of an implementation of the random rodon transformation, some tests for it. Current algorithm can process binary square images that have a number of lines (they can have different thickness) and returns a square black and white image where each point represents a line with curtain probability (the measure of our confidence in the presence of a particular line).

The main idea of the algorithm is to select two random points, calculate parameters of the resulting line (basic geometry), store this information and repeat this iteration. The last step is to count the frequency of getting a line with parameters represented by each point in the transformed image and colour all pixels grey (darkness is proportional to calculated frequency).

