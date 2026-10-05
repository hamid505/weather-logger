temps = []

while True:
    temperature = input("Enter temperature ('done' to stop): ")

    if temperature == "done":
        break

    temps.append(float(temperature))


def summarize(temps):
    return {
        "minimum": min(temps),
        "maximum": max(temps),
        "average": sum(temps) / len(temps)
    }


print(summarize(temps))