# TASK: DNA
"""
    This challenge will put emphasis on your knowledge of classes, inheritance and polymorphism

        1. Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
            - A Gene is a single value 0 or 1, it can mutate (flip).
            - A Chromosome is a series of 10 Genes. It also can mutate,
                meaning a random number of genes can randomly flip (1/2 chance to flip).
            - A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.

        2. Implement these classes as you see fit.

        3. Create a new class called Organism that accepts a DNA object and an environment parameter that sets
            the probability for its DNA to mutate.

        4. Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s.
            Then stop and record the number of generations (iterations) it took.

    Write your results in you personal biology research notebook and tell us your conclusion :).
"""
from random import randint


class Gene:
    def __init__(self):
        self.gene = randint(0, 1)

    def flip(self):
        chance = randint(0, 1)
        if chance:
            self.gene = 0
        else:
            self.gene = 1

        return self.gene

    def get_item(self):
        return self.gene


class Chromosome(Gene):
    def __init__(self):
        super().__init__()
        self.chromosome = [Gene().get_item() for n in range(10)]

    def mutate(self):
        self.chromosome = [not gene for gene in self.chromosome]
        return self.chromosome

    def get_item(self):
        return self.chromosome


class DNA(Chromosome):
    def __init__(self):
        super().__init__()
        self.dna = [Chromosome() for n in range(10)]

    def all_ones(self):
        return all([all(chromosome.mutate()) for chromosome in self.dna])

    def get_item(self):
        return [chromosome.get_item() for chromosome in self.dna]


class Organism(DNA):
    def __init__(self):
        super().__init__()
        self.organism = [DNA() for n in range(10)]

    def get_item(self):
        return [dna.get_item() for dna in self.organism]


def get_it(item):
    print(item.get_item())
    return item.get_item()


a = Gene()
print(f"Gene: {a.get_item()}\n")
#
b = Chromosome()
print(f"Chromosome: {b.get_item()}\n"
      f"Inverse chromosome: {b.mutate()}\n")

c = DNA()
print(f"DNA: {c.get_item()}"
      f"All ones?: {c.all_ones()}\n")

d = Organism()
print(f"Organism: {d.get_item()}\n"
      f"All ones?: {d.all_ones()}\n"
      f"Mutation: {d.mutate()}\n")

counter = -1
while not d.all_ones():
    # print("in loop:", d.get_item())
    counter += 1
    d.mutate()

print(counter)
