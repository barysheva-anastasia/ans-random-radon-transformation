# Random-Radon-Transformation

Repository consists of implementation of the random rodon transformation, some tests for it. Current algorithm can process binary square images that of a number of lines (they can have different thickness) and returns square black and white picture where each point represents a line with curtain probability (the measure of our confidence in presence of a particular line)

The main idea of the algorithm is to choose two random points calculate parameters of the resulting line (basic geometry) save this information and repeat this iteration. The last step is to count frequency of getting a line with parameters represented by each point in transformed image and color all pixels grey (darkness is proportional to calculated frequensy)
