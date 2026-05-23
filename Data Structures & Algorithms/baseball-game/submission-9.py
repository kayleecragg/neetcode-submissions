class Solution:
    def calPoints(self, operations: List[str]) -> int:

        scores = []

        for operation in range(len(operations)):
            # assuming if its not one of these special characters, its a valid number :eyebrow:
            if (
                operations[operation] != "+"
                and operations[operation] != "D"
                and operations[operation] != "C"
            ):
                scores.append(int(operations[operation]))

            else:
                if operations[operation] == "+":
                    scores.append(scores[(len(scores) - 1)] + scores[(len(scores) - 1) - 1])

                elif operations[operation] == "D":
                    scores.append((scores[(len(scores) - 1)] * 2))

                elif operations[operation] == "C":
                    scores.pop()

        final = 0

        for scorey in scores:
            final += scorey

        return final
