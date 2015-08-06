class GreaterGameDiv2:
    def calc(self, snuke, sothe):
        total = 0
        for i in range(len(snuke)):
            if snuke[i] > sothe[i]:
                total += 1
        return total
