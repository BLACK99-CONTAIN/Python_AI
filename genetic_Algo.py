import random

class Queen:
    def __init__(self, board_size=8):
        self.board_size = board_size
        self.genome = random.sample(range(board_size), board_size)
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        conflicts = 0
        for i in range(self.board_size):
            for j in range(i + 1, self.board_size):
                if self.genome[i] == self.genome[j] or abs(self.genome[i] - self.genome[j]) == abs(i - j):
                    conflicts += 1
        return (self.board_size * (self.board_size - 1)) // 2 - conflicts

    def mutate(self):
        idx1, idx2 = random.sample(range(self.board_size), 2)
        self.genome[idx1], self.genome[idx2] = self.genome[idx2], self.genome[idx1]
        self.fitness = self.calculate_fitness()

    def crossover(self, other):
        crossover_point = random.randint(1, self.board_size - 1)
        child_genome = self.genome[:crossover_point] + other.genome[crossover_point:]
        child = Queen(self.board_size)
        child.genome = child_genome
        child.fitness = child.calculate_fitness()
        return child

def genetic_algorithm(population_size=100, generations=1000, mutation_rate=0.1, board_size=8):
    population = [Queen(board_size) for _ in range(population_size)]
    max_fitness = (board_size * (board_size - 1)) // 2  # Maximum fitness for a solution

    for generation in range(generations):
        population.sort(key=lambda q: q.fitness, reverse=True)
        print(f"Generation {generation}: Best fitness = {population[0].fitness}")

        if population[0].fitness == max_fitness:
            print("Solution found:")
            print(population[0].genome)
            return population[0]

        new_population = []
        while len(new_population) < population_size:
            parent1 = random.choice(population[:20])  # Select from the top 20
            parent2 = random.choice(population[:20])

            child = parent1.crossover(parent2)
            if random.random() < mutation_rate:
                child.mutate()
            new_population.append(child)

        population = new_population

    print("No solution found in the given generations.")
    return None

# Run the Genetic Algorithm
result = genetic_algorithm(population_size=200, generations=1000, mutation_rate=0.1)
