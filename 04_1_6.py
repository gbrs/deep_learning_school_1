class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f
        self.x = None

    def forward(self, x):
        self.x = x
        return self.f(
                        sum(
                            [self.w[i] * x[i] for i in range(len(x))]
                        )
                )

    def backlog(self):
        return self.x


