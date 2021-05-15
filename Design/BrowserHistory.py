class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.at = 0

    def visit(self, url: str) -> None:
        self.urls[self.at+1:] = [url]
        self.at += 1

    def back(self, steps: int) -> str:
        self.at = max(0, self.at-steps)
        return self.urls[self.at]

    def forward(self, steps: int) -> str:
        self.at = min(len(self.urls)-1, self.at+steps)
        return self.urls[self.at]


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]
