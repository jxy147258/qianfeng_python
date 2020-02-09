class animal():
    def run(self):
        print("animal is running")


class dog():
    def run(self):
        print("dog is running")


class cat():
    def run(self):
        print("cat is running")


def run_twice(animal):
    animal.run()


a = animal()
d = dog()
c = cat()
run_twice(a)
run_twice(d)
run_twice(c)

