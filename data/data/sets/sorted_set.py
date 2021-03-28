def observed():
    observations = []
    for i in range(0, 5, 1):
        observations.append(input())
    return observations


def remove_observations(observations):
    is_running = True
    while (is_running):
        remove = input("Do you wish to remove any observations yes/no?")
        if (remove == "yes"):
            observation = input("What observation do you wish to remove?")
            observations.remove(observation)
        else:
            is_running = False


def run():
    observations = observed()
    remove_observations(observations)
    observation_set = set()
    for observation in observations:
        observation_tuple = (observation, observations.count(observation))
        observation_set.add(observation_tuple)
        sorted(observation_set)
    print(observation_set)


if __name__ == "__main__":
    run()
