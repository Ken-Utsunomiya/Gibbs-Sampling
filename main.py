
import random

factors = {
    "AB": [[30,5],
           [1,10]],
    "BC": [[100,1],
           [1,100]],
    "CD": [[1,100],
           [100,1]],
    "DA": [[100,1],
           [1,100]],
}

random_variables = ["A", "C", "D"]

def random_assignment():
    a = random.randint(0,1)
    b = 1
    c = random.randint(0,1)
    d = random.randint(0,1)

    return {
        "A": a,
        "B": b,
        "C": c,
        "D": d
    }

if __name__ == '__main__':
    initial_assignment = random_assignment()
    current_assignment = initial_assignment.copy()
    samples = [initial_assignment]
    sample_count = 100000

    for i in range(sample_count):
        variable = random_variables[i%3]
        factor = []

        if variable == "A":
            factor = [a*b for a,b in zip([factors["AB"][0][current_assignment["B"]],factors["AB"][1][current_assignment["B"]]],
                                         factors["DA"][current_assignment["D"]])]
        elif variable == "C":
            factor = [a*b for a,b in zip([factors["CD"][0][current_assignment["D"]],factors["CD"][1][current_assignment["D"]]],
                                         factors["BC"][current_assignment["B"]])]
        else:
            factor = [a*b for a,b in zip([factors["DA"][0][current_assignment["A"]],factors["DA"][1][current_assignment["A"]]],
                                         factors["CD"][current_assignment["C"]])]

        prob = [x / sum(factor) for x in factor]

        current_assignment = current_assignment.copy()

        if random.uniform(0,1) <= prob[0]:
            current_assignment[variable] = 0
        else:
            current_assignment[variable] = 1

        samples.append(current_assignment)

    result = [0,0]
    for sample in samples:
        result[sample["A"]] += 1

    print(result)



